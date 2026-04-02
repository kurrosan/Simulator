## 1. Разработка фронтенда сайта (CSS, HTML, JavaScript)
Начать нужно с создания шаблона сайта, у нас был примерно такой (чуть позже с помощью ИИ был переработан в более классичский дизайн):

<img width="1239" height="693" alt="image" src="https://github.com/user-attachments/assets/537d6ddf-211e-45c6-8a1a-94ffffe1697a" />
<img width="1228" height="686" alt="image" src="https://github.com/user-attachments/assets/caa026f0-748d-4ccd-90e0-4dbd616386b1" />

Теперь нужно загрузить эти изображения в генеративную нейросеть и написать промпт:
```bash
На основе этих фото разработатй нам код для сайта с тестирвоанием
```
Там нам выдали код
```bash
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Тест: Сборка ПК</title>

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: white;
    text-align: center;
}

.container {
    max-width: 800px;
    margin: auto;
    padding: 40px 20px;
}

h1, h2 {
    margin-bottom: 20px;
}

button {
    padding: 12px 25px;
    margin: 10px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
    transition: 0.3s;
}

.start-btn {
    background: #00c853;
    color: white;
    font-size: 20px;
}

.answer-btn {
    background: white;
    color: black;
    display: block;
    width: 100%;
}

.answer-btn:hover {
    background: #ffd600;
}

.hidden {
    display: none;
}

.result {
    font-size: 22px;
    margin-top: 20px;
}

input {
    padding: 8px;
    margin: 10px;
    border-radius: 5px;
    border: none;
}
</style>
</head>

<body>

<div class="container">

<!-- Стартовый экран -->
<div id="start-screen">
    <h1>Тест</h1>
    <p>Изучение порядка сборки ПК и подключения оборудования</p>
    <p><strong>Разработчики:</strong> Григорьева А.Г., Поливанчук П.Н.</p>
    <button class="start-btn" onclick="startQuiz()">НАЧАТЬ</button>
</div>

<!-- Экран вопросов -->
<div id="quiz-screen" class="hidden">
    <h2 id="question-title"></h2>
    <div id="answers"></div>
</div>

<!-- Результат -->
<div id="result-screen" class="hidden">
    <h2>Тест закончен</h2>
    <div class="result" id="score"></div>
    <button onclick="location.reload()">Пройти снова</button>
</div>

</div>

<script>
let currentQuestion = 0;
let score = 0;

const quizData = [

{
    question: "С чего рекомендуется начинать сборку ПК?",
    answers: [
        { text: "Установки видеокарты", correct: false },
        { text: "Установки процессора на материнскую плату", correct: true },
        { text: "Установки блока питания в корпус", correct: false },
        { text: "Подключения монитора", correct: false }
    ]
},

{
    question: "Перед началом сборки ПК необходимо отключить питание",
    answers: [
        { text: "Да", correct: true },
        { text: "Нет", correct: false }
    ]
},

{
    question: "Расположите этапы сборки ПК в правильном порядке (введите буквы подряд без пробелов): а, б, в, г, д",
    input: true,
    correctAnswer: "бгавд"
},

{
    question: "Соотнесите компонент и его назначение (введите ответ в формате 1-В,2-Б,3-А,4-Г)",
    input: true,
    correctAnswer: "1-в,2-б,3-а,4-г"
}

];

function startQuiz() {
    document.getElementById("start-screen").classList.add("hidden");
    document.getElementById("quiz-screen").classList.remove("hidden");
    showQuestion();
}

function showQuestion() {
    const questionData = quizData[currentQuestion];
    document.getElementById("question-title").innerText = questionData.question;
    const answersDiv = document.getElementById("answers");
    answersDiv.innerHTML = "";

    if (questionData.input) {
        const input = document.createElement("input");
        input.type = "text";
        input.id = "textAnswer";
        answersDiv.appendChild(input);

        const btn = document.createElement("button");
        btn.innerText = "Ответить";
        btn.className = "answer-btn";
        btn.onclick = checkInputAnswer;
        answersDiv.appendChild(btn);

    } else {
        questionData.answers.forEach(answer => {
            const btn = document.createElement("button");
            btn.innerText = answer.text;
            btn.className = "answer-btn";
            btn.onclick = () => selectAnswer(answer.correct);
            answersDiv.appendChild(btn);
        });
    }
}

function selectAnswer(correct) {
    if (correct) score++;
    nextQuestion();
}

function checkInputAnswer() {
    const userAnswer = document.getElementById("textAnswer").value
        .toLowerCase()
        .replace(/\s/g, "");

    const correct = quizData[currentQuestion].correctAnswer
        .toLowerCase()
        .replace(/\s/g, "");

    if (userAnswer === correct) score++;
    nextQuestion();
}

function nextQuestion() {
    currentQuestion++;
    if (currentQuestion < quizData.length) {
        showQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    document.getElementById("quiz-screen").classList.add("hidden");
    document.getElementById("result-screen").classList.remove("hidden");
    document.getElementById("score").innerText =
        "Оценка: " + score + " из " + quizData.length;
}
</script>

</body>
</html>
```
Теперь у нас есть простой дизайн ✨
## 2. Генерация backend
Теперь нам нужно описать backend-часть сайта, для этого просим сделать полный сайт 
```bash
Сделай сайт на Fast API, используя язык программирования Python
```
Нейросеть нам выдаст полный код, который можно запустить и он будет работать.
Структура сайта:

<img width="922" height="291" alt="image" src="https://github.com/user-attachments/assets/23c49263-9630-4625-891d-93d9fa5773a9" />

```bash
pc_quiz/
│
├── main.py
├── templates/
│     ├── index.html
│     └── result.html
└── static/
      └── style.css
```
Теперь эту структуру нужно создать в PyCharm как на изображении:

<img width="313" height="661" alt="image" src="https://github.com/user-attachments/assets/496aa871-ecc8-4013-bc54-eec0bbb401e8" />

Далее в терминале нужно установить библиотеки

<img width="50" height="57" alt="image" src="https://github.com/user-attachments/assets/276fc190-9039-45b8-9bf3-3a9910ecd171" />

```bash
pip install annotated-doc==0.0.4 annotated-types==0.7.0 anyio==4.12.1 charset-normalizer==3.4.4 click==8.3.1 colorama==0.4.6 fastapi==0.135.1 greenlet==3.3.2 h11==0.16.0 idna==3.11 itsdangerous==2.2.0 Jinja2==3.1.6 MarkupSafe==3.0.3 pillow==12.1.1 pydantic==2.12.5 pydantic_core==2.41.5 python-multipart==0.0.22 reportlab==4.4.10 SQLAlchemy==2.0.48 starlette==0.52.1 typing-inspection==0.4.2 typing_extensions==4.15.0 uvicorn==0.30.6
```

Далее берем код для main.py и копируем его к себе:

<img width="802" height="725" alt="image" src="https://github.com/user-attachments/assets/4869bcf8-f501-4126-a34f-f1707f5147c1" />

```bash
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


CORRECT_ANSWERS = {
    "q1": "b",
    "q2": "yes",
    "q3": "бгавд",
    "q4": "1-в,2-б,3-а,4-г"
}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit", response_class=HTMLResponse)
async def submit(
    request: Request,
    q1: str = Form(...),
    q2: str = Form(...),
    q3: str = Form(...),
    q4: str = Form(...)
):
    score = 0

    if q1.lower() == CORRECT_ANSWERS["q1"]:
        score += 1

    if q2.lower() == CORRECT_ANSWERS["q2"]:
        score += 1

    if q3.lower().replace(" ", "") == CORRECT_ANSWERS["q3"]:
        score += 1

    if q4.lower().replace(" ", "") == CORRECT_ANSWERS["q4"]:
        score += 1

    return templates.TemplateResponse("result.html", {
        "request": request,
        "score": score
    })
```


 Также меняем вначале index.html
 
```bash
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Тест: Сборка ПК</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

<div class="container">
    <h1>Тест</h1>
    <p>Изучение порядка сборки ПК и подключения оборудования</p>

    <form action="/submit" method="post">

        <h3>1. С чего рекомендуется начинать сборку ПК?</h3>
        <label><input type="radio" name="q1" value="a"> Установка видеокарты</label><br>
        <label><input type="radio" name="q1" value="b"> Установка процессора</label><br>
        <label><input type="radio" name="q1" value="c"> Установка блока питания</label><br>
        <label><input type="radio" name="q1" value="d"> Подключение монитора</label>

        <h3>2. Перед началом сборки ПК необходимо отключить питание</h3>
        <label><input type="radio" name="q2" value="yes"> Да</label><br>
        <label><input type="radio" name="q2" value="no"> Нет</label>

        <h3>3. Введите правильный порядок этапов (бгавд)</h3>
        <input type="text" name="q3" required>

        <h3>4. Соотнесите компонент и назначение (1-в,2-б,3-а,4-г)</h3>
        <input type="text" name="q4" required>

        <br><br>
        <button type="submit">Завершить тест</button>

    </form>
</div>

</body>
</html>
```
 Потом result.html
```bash
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Результат</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

<div class="container">
    <h1>Тест закончен</h1>
    <h2>Ваш результат: {{ score }} / 4</h2>

    <a href="/">Пройти снова</a>
</div>

</body>
</html>
```
И стили из кода выше добавляем в style.css
```bash
/* ===== ОСНОВА ===== */

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #1e1b4b, #312e81, #be185d);
    background-size: 200% 200%;
    animation: gradientMove 12s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    color: white;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ===== СТАРТОВЫЙ ЭКРАН ===== */

.start-screen {
    text-align: center;
}

.start-screen h1 {
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 10px;
    background: linear-gradient(90deg, #60a5fa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.start-screen p {
    opacity: 0.9;
    margin-bottom: 30px;
}

.start-screen button {
    padding: 16px 50px;
    font-size: 18px;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    background: linear-gradient(90deg, #3b82f6, #ec4899);
    color: white;
    font-weight: 600;
    transition: 0.3s;
    box-shadow: 0 0 20px rgba(236,72,153,0.6);
}

.start-screen button:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 35px rgba(236,72,153,0.9);
}

/* ===== МОДАЛЬНОЕ ОКНО ===== */

.modal {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(10, 10, 30, 0.7);
    backdrop-filter: blur(8px);
    justify-content: center;
    align-items: center;
}

.modal-content {
    width: 95%;
    max-width: 750px;
    padding: 40px;
    border-radius: 24px;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(25px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    animation: modalFade 0.4s ease;
}

@keyframes modalFade {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
}

/* ===== ПРОГРЕСС ===== */

.progress {
    height: 8px;
    background: rgba(255,255,255,0.15);
    border-radius: 50px;
    margin-bottom: 30px;
    overflow: hidden;
}

#progressBar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #60a5fa, #f472b6);
    border-radius: 50px;
    transition: width 0.4s ease;
}

/* ===== ВОПРОСЫ ===== */

.question {
    display: none;
}

.question.active {
    display: block;
}

h3 {
    margin-bottom: 20px;
    font-weight: 600;
}

/* ===== ВАРИАНТЫ ===== */

label {
    display: block;
    padding: 14px;
    margin: 10px 0;
    border-radius: 14px;
    background: rgba(255,255,255,0.1);
    cursor: pointer;
    transition: 0.3s;
}

label:hover {
    background: rgba(236,72,153,0.25);
    transform: translateX(4px);
}

input[type="radio"] {
    margin-right: 10px;
}

/* ===== ПОЛЯ ВВОДА ===== */

input[type="text"] {
    width: 100%;
    padding: 14px;
    border-radius: 14px;
    border: none;
    margin-bottom: 20px;
    background: rgba(255,255,255,0.15);
    color: white;
    font-size: 15px;
}

/* ===== КНОПКИ ===== */

button {
    padding: 12px 30px;
    border-radius: 40px;
    border: none;
    background: linear-gradient(90deg, #3b82f6, #ec4899);
    color: white;
    font-weight: 600;
    cursor: pointer;
    transition: 0.3s;
    box-shadow: 0 0 15px rgba(236,72,153,0.5);
}

button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 30px rgba(236,72,153,0.8);
}

/* ===== РЕЗУЛЬТАТ ===== */

.result-score {
    text-align: center;
    font-size: 28px;
    margin-bottom: 20px;
    background: linear-gradient(90deg, #60a5fa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.result-bar {
    height: 14px;
    background: rgba(255,255,255,0.15);
    border-radius: 50px;
    overflow: hidden;
    max-width: 600px;
    margin: auto;
}

.result-fill {
    height: 100%;
    width: 0;
    background: linear-gradient(90deg, #60a5fa, #f472b6);
    border-radius: 50px;
    transition: width 1s ease;
}

/* ===== АДАПТИВНОСТЬ ===== */

@media (max-width: 600px) {
    .modal-content {
        padding: 25px;
    }

    .start-screen h1 {
        font-size: 36px;
    }
}
```
Теперь мы можем запустить сайт используя команду в терминале:

```bash
uvicorn main:app --reload
```
Сайт можно оставить и так, но можно улучшить его 😉
## 3. Улучшение и тестирование сайта
Далее мы можем улучшить дизайн сайта, тут можно сколько угодно писать улучшения нейросети, но не забывайте проверять работоспособность модулей!

Генеративные нейросети для текста всегда предлагают вам варианты улучшения можно выбрать из этого, а можно придумать что-то свое, я же просила сделать более современный стиль, и выбирала варианты, предложенные нейросетью, для улучшения своего сайта.

<img width="607" height="264" alt="image" src="https://github.com/user-attachments/assets/4e886ca6-f4e4-4dcc-a2e5-ef5a1e6884f7" />

Теперь как сделать так чтобы без потерь в коде добавить улучшения? А нужно писать два этих промпта ВСЕГДА, в не зависимости от  того устроил вас результат или нет.

1. Промпт на добавление улучшения например:

```bash
Нужно, чтобы каждый вопрос был с новой страницы, можно сделать в модальном окне.
```

2. Промпт на получение готового результата, а именно всего кода, которрый нужно изменить

```bash
Напиши полностью коды.
```
И так нужно делать пока вас не устроит реззультат. 

❗️При появлении ошибок в коде или на сайте отправьте эту ошибку в нейросеть и она даст вам варианты решения проблемы❗️

## 4. Хостинг
Теперь допустим нас устраивает сайт и мы хотим его выложить в сеть, для использования в работе. Хостинг зачастую платный, но есть хостинги с пробмным периодом. Я же использую [TimeWebCloud](https://timeweb.cloud/). Но пока нам нужно загрузить проект на GitHub.

```bash
pip freeze > requirements.txt
```

<img width="1918" height="856" alt="image" src="https://github.com/user-attachments/assets/b3bf748b-a098-463a-bc43-bc92b71aff25" />

Создадим файл requirements.txt для автоматической установки библиотек во время хостинга.

Теперь нужно войти в аккаунт на [GitHub](https://github.com/), если его нет, то создать.

После этого нужно отправить файлы в GitHub, для этого заходим на вкладку под номером 1, там выбираем все файлы, затем в месте под номером 2 пишем текст комита и нажимает на кнопку под номером 3.

<img width="378" height="382" alt="image" src="https://github.com/user-attachments/assets/8798a37a-9fe8-4c53-8c1b-384fd22188c1" />

Все у нас создан репозиторий и мы можем захостить сайт.

<img width="1623" height="912" alt="image" src="https://github.com/user-attachments/assets/30d816fe-5769-427f-bf00-82c23bc5f1dd" />

Для хостинга нужно создать аккаунт на сайте [TimeWebCloud](https://timeweb.cloud/).

Далее выбираем выделенную красным цветом кнопку

<img width="351" height="505" alt="image" src="https://github.com/user-attachments/assets/ca7856c4-a95e-4ab9-817f-50a20727bb5c" />

Далее заполняем все также как и тут

<img width="525" height="781" alt="image" src="https://github.com/user-attachments/assets/4de09050-c531-4125-8274-9a5b051ff97e" />

<img width="520" height="265" alt="image" src="https://github.com/user-attachments/assets/e939c344-e86d-442f-9b4a-6febade48e74" />

<img width="561" height="699" alt="image" src="https://github.com/user-attachments/assets/c36acf02-45f2-47b3-8ea2-c9d945ccbca7" />

<img width="425" height="504" alt="image" src="https://github.com/user-attachments/assets/b731dede-f179-4286-be0f-718e66df3cd6" />

Ну и теперь ждем, когда закогчится хостинг. Во время хостинга могут появляться ошибки, можно с ними обратиться в поддержку.

В конце сайт будет доступен по вашей ссылке, в моем случае : https://kurrosan-simulator-1c87.twc1.net/

