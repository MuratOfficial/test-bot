<h1 align="center">🤖 Telegram Test Bot (Учебный проект)</h1>
<p align="center">
  Telegram-бот, разработанный с использованием фреймворка aiogram, предназначен для обучения и практики создания ботов на Python.
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/MuratOfficial/test-bot?style=flat-square" />
  <img src="https://img.shields.io/github/license/MuratOfficial/test-bot?style=flat-square" />
  <img src="https://img.shields.io/github/stars/MuratOfficial/test-bot?style=flat-square" />
</p>

---

## 🚀 О проекте

**Test Bot** — это простой Telegram-бот, созданный для изучения основ работы с фреймворком aiogram. Проект демонстрирует базовую структуру бота, обработку команд и сообщений, а также организацию кода с использованием хендлеров.

---

## 🧰 Стек технологий

- **Язык программирования**: Python 3.8+
- **Фреймворк**: aiogram
- **Библиотеки**: asyncio, logging
- **Инструменты разработки**: Python-telegram-bot API

---

## ⚙️ Функциональность

- ✅ Обработка команд `/start` и `/help`
- ✅ Ответы на текстовые сообщения
- ✅ Структурированная организация кода с использованием хендлеров
- ⏳ Подключение базы данных для хранения информации (в планах)
- ⏳ Реализация inline-кнопок и клавиатур (в планах)

---

## 📦 Установка и запуск

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/MuratOfficial/test-bot.git
cd test-bot

# 2. Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Создайте файл .env и добавьте ваш токен бота
echo "BOT_TOKEN=your_bot_token_here" > .env

# 5. Запустите бота
python tgbot.py
```

## 🗂️ Структура проекта

```text
test-bot/
├── handlers/           # Хендлеры для обработки сообщений и команд
│   ├── start.py
│   └── help.py
├── kb/                 # Клавиатуры (в разработке)
├── create_bot.py       # Инициализация бота и диспетчера
├── tgbot.py            # Точка входа в приложение
├── .env                # Файл с переменными окружения
├── .gitignore
└── requirements.txt    # Список зависимостей
```

## 🤝 Вклад

Хочешь внести свой вклад? Добро пожаловать!
```bash
# Форкни репозиторий
# Создай новую ветку
git checkout -b feature/my-feature

# Внеси изменения и сделай коммит
git commit -m "Добавил новую фичу"

# Отправь изменения
git push origin feature/my-feature

# Создай Pull Request!
```

<p align="center"><b>Создано с ❤️ в учебных целях by <a href="https://github.com/MuratOfficial">MuratOfficial</a></b></p>
