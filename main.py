from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from starlette.middleware.sessions import SessionMiddleware
from datetime import datetime

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="secret-key")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ================= DATABASE =================
DATABASE_URL = "sqlite:///./simulator_work6.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Test(Base):
    __tablename__ = "tests"
    id = Column(Integer, primary_key=True, index=True)
    group = Column(String)
    subject = Column(String)
    title = Column(String)

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    score = Column(Integer)
    percent = Column(Integer)
    grade = Column(String)
    time_spent = Column(String)
    date = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ================= AUTH =================
ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "1234"

# ================= HOME =================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(get_db)):
    tests = db.query(Test).all()
    is_admin = request.session.get("admin", False)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tests": tests, "is_admin": is_admin}
    )

# ================= LOGIN =================
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, login: str = Form(...), password: str = Form(...)):
    if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:
        request.session["admin"] = True
    return RedirectResponse("/", status_code=303)

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)

# ================= CREATE / EDIT / DELETE TEST =================
@app.get("/create-test", response_class=HTMLResponse)
async def create_test_page(request: Request):
    if not request.session.get("admin"):
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("create_test.html", {"request": request})

@app.post("/create-test")
async def create_test(request: Request, group: str = Form(...), subject: str = Form(...), title: str = Form(...), db: Session = Depends(get_db)):
    test = Test(group=group, subject=subject, title=title)
    db.add(test)
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/edit-test/{test_id}", response_class=HTMLResponse)
async def edit_test_page(request: Request, test_id: int, db: Session = Depends(get_db)):
    if not request.session.get("admin"):
        return RedirectResponse("/", status_code=303)
    test = db.get(Test, test_id)
    return templates.TemplateResponse("edit_test.html", {"request": request, "test": test})

@app.post("/edit-test/{test_id}")
async def edit_test(request: Request, test_id: int, group: str = Form(...), subject: str = Form(...), title: str = Form(...), db: Session = Depends(get_db)):
    test = db.get(Test, test_id)
    test.group = group
    test.subject = subject
    test.title = title
    db.commit()
    return RedirectResponse("/", status_code=303)

@app.get("/delete-test/{test_id}")
async def delete_test(request: Request, test_id: int, db: Session = Depends(get_db)):
    if not request.session.get("admin"):
        return RedirectResponse("/", status_code=303)
    test = db.get(Test, test_id)
    db.delete(test)
    db.commit()
    return RedirectResponse("/", status_code=303)

# ================= TEST PAGE =================
@app.get("/test/{test_id}", response_class=HTMLResponse)
async def open_test(request: Request, test_id: int, db: Session = Depends(get_db)):
    test = db.get(Test, test_id)
    return templates.TemplateResponse("quiz.html", {"request": request, "test": test})

# ================= SUBMIT TEST =================
@app.post("/submit")
async def submit_test(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    name = form.get("name")
    time_spent = form.get("time_spent")
    score = 0

    # проверка ответов
    if form.get("q1") == "b": score += 1
    if form.get("q2") == "b": score += 1
    if form.get("q3") == "b": score += 1
    if form.get("q4") == "c": score += 1
    if form.get("q5") == "false": score += 1
    if form.get("q6") == "true": score += 1
    if form.get("q7") == "true": score += 1

    percent = int((score / 5) * 100)

    if percent >= 90:
        grade = "Отлично"
    elif percent >= 70:
        grade = "Хорошо"
    elif percent >= 50:
        grade = "Удовлетворительно"
    else:
        grade = "Не сдано"

    # сохраняем в БД
    res = Result(
        name=name,
        score=score,
        percent=percent,
        grade=grade,
        time_spent=time_spent,
        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    db.add(res)
    db.commit()

    # сохраняем в сессию для результата
    request.session["result"] = {
        "name": name,
        "score": score,
        "percent": percent,
        "grade": grade,
        "time_spent": time_spent
    }

    return RedirectResponse("/result", status_code=303)
# ================= RESULT PAGE =================
@app.get("/result", response_class=HTMLResponse)
async def result_page(request: Request):
    result = request.session.get("result")
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "name": result["name"],
            "score": result["score"],
            "percent": result["percent"],
            "grade": result["grade"],
            "time_spent": result["time_spent"]
        }
    )

# ================= LEADERBOARD =================
@app.get("/leaderboard", response_class=HTMLResponse)
async def leaderboard(request: Request, db: Session = Depends(get_db)):
    results = db.query(Result).order_by(Result.score.desc(), Result.date.asc()).all()
    return templates.TemplateResponse(
        "leaderboard.html",
        {"request": request, "results": results}
    )

from fastapi.responses import Response

CERT_TOPIC = "Изучение порядка сборки ПК и подключения оборудования"

@app.get("/certificate/{user_name}", response_class=Response)
async def certificate(user_name: str):
    # Загружаем SVG-шаблон
    with open("templates/certificate.svg", "r", encoding="utf-8") as f:
        svg = f.read()

    # Подставляем имя и тему
    svg = svg.replace("{FULL_NAME}", user_name)
    svg = svg.replace("{TOPIC}", CERT_TOPIC)

    return Response(content=svg, media_type="image/svg+xml")
