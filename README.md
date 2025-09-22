# Тестовое задание Диамант Вижн

[Ссылка на Google Таблицу](https://docs.google.com/spreadsheets/d/1CxmOZHa_8KmLdo3QgQKQjYEX2F3-1BUZVqSk9ur-cW0/edit?gid=0#gid=0)

Telegram Bot - @diamant_vision_test_project_bot

## Пример запросов к API через curl

### Создать жалобу

```bash
curl -X POST http://localhost:8000/api/v1/issues -H "Content-Type: application/json" -d '{"text": "I cant use my headphones"}'
```

### Получить список открытых жалоб за последний час
```bash
curl -X GET http://localhost:8000/api/v1/issues\?status\=open
```

### Закрыть жалобу
```bash
curl -X POST http://localhost:8000/api/v1/issues/24/close
```

## 📁 Подготовка окружения

### 1. Клонировать репозиторий
```bash
git clone https://github.com/HanSaloZu/diamant-vision-test-project.git
cd diamant-vision-test-project
```

### 2. Создать `.env` файл

В корне проекта необходимо создать файл `.env` и заполнить его следующими переменными:

```env
DB_NAME='db.sqlite3' # Имя базы данных
SENTIMENT_ANALYSIS_API_KEY='' # API-ключ Sentiment Analysis API
CHAT_GPT_API_KEY='' # API-ключ ChatGPT
TELEGRAM_API_KEY='' # API-ключ Telegram-бота
GOOGLE_SERVICE_ACCOUNT_EMAIL='' # Сервисный Google-аккаунт
GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY='' # Ключ сервисного Google аккаунта
```

## Запуск

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Создание БД и применение миграций
```bash
alembic upgrade head
```

### 3. Запуск проекта
```bash
python main.py
```
