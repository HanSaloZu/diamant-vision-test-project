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
SENTIMENT_ANALYSIS_API_KEY='QP4H2HdnLUvN2ooha0Ya16lY31DGQhNF' # API-ключ Sentiment Analysis API
CHAT_GPT_API_KEY='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' # API-ключ ChatGPT
TELEGRAM_API_KEY='7638946258:AAEkMGfdvRNBql0Q7MLuj0EVIHY-DgWkbE0' # API-ключ Telegram-бота
GOOGLE_SERVICE_ACCOUNT_EMAIL='n8n-workflow@diamant-vision-test-project.iam.gserviceaccount.com' # Сервисный Google-аккаунт
GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY='-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC0Ao05uhBWPCcF\n780Rnxx2za+C1YeIRfuY3sAUci9vxMvvLYZZ6V4njz/tFgcbrCt5WZuLnjslyPAI\nSRq9xw8W1jNiiMgsjlkRxngn4qnKwouupab+0znSLUWC/QDEDsrwVopA6qwe3uCO\ndKLJ5FtHW3hkKrn7QHGZd4akc1ADaYlhb4LYz6MRuSqlS90D8uvatq4ZrnJ8zlzV\n1ct2cGQiPz+P+uv0uimxWL7MVOM08/d7ZBhhv0bG6J+lGQp0pnc8sqKZy7yBSpIF\nIe92qYjG+uoAnmGxRJe3OaA/AbJ6C6u1yXcLaCNnhZsNja2o9TerYHC03YJmsvSV\nnEq1jdZVAgMBAAECggEAFMe0oOTbTPEtuhA4NqANC6Pr7mkS98bIaBnSx6l002y+\n9BHn0ApSHbP6N7bSxD2IWT5gZ+owvshm+TXjOeQ4WDULAoVywj3+h0BHj6cpXag+\nsr8Zu5ILuzkRrLDjPT7N65e55wuQKhIljxxkzHSpmt+y0rFh/eCvHH3BU8uiAXqk\nVZtAFcbXUlrDSINSk6lUuH+9WmgLc02s2OeBsYnGLeIWJsSwNWJgcD8Wuo3EgB3u\nnxCUnV2uYlne/chrL3BmVZqj9eP7PWXqSIvW8d7hdxbVruFWVfMohRatwRwUJA9I\n4asUGFuvPOCQQZuvUNC7gFdMieLit6sbenWD0pJp0QKBgQDc3mLThbhaYmvDx/IS\nj9JVWSfiW2C4JKMeZfLxN5GvzGC4nfHQ8xcORdo8gjl9gS22UF/nSUOZ9xDVhTmI\nm/49EK1wg3L9oIfsRzbQwTDh+bb/YD4pSE8hMyMvAMzcREs3fnnaFjX0ehwkS6x9\nnDGm+vbORby7If7mJzEO/kkaaQKBgQDQpG19BhQd4+Z/EPd9Kyi/L1VPeBOiGtET\n83PYIROrkOyV6BwOMkJal0eF+RUeV5o9jChtDtz3m/pTjTTDPiJFX0S9qs/iWBWL\nP4ewFf/j1E9yLGm4skTHoj9S4XZsQlM158J3d7dH9xz8ZNyJnll5EV1fU9LQA3yk\nWPdHSRWnDQKBgAjVSASHm4jZ2M96pp7Ba7sIFsVBvEuBA5kKoL2u6D+sn82iW3Js\n1mY2uvSijKQNT4O0ETHRx0dYDy9K5bMl8fQFP7p5N1cXXXhAnNuablcLQptSAQpr\nnuaIAgc2M/s3K/7rKvpi2wONAqUc9agMYBv6e3ZiaZreUDBqLtcXqlrJAoGAXaUf\ne1kKGGxc3TVZT7XaYQ02pieH8F9G7kR7/0rBUGUIuzPlu711KMHzmT816lt5YByT\nXHeqV/yLO4sKXoN50Fc1PEf5bGcKrGhEV5VYOALn8Z/bh8mDs3KwJ1wI0ghm3q/6\nCbMS8VsJiIMgtSf8kqlnlkzCNxkJjZ5cxoMYE9UCgYBGTk7sC4MKA+fgW6uVXvTr\n+zhTdV3sZn8K+EFjM9XYtGFNACXHZIfqws0AvjrfTt6jxumg26nTEwl/PMkB2Nja\neO4Fuv0kia5m5O5BgBl+CO9LIcq1PUAqqqs1qFDg9srHQgl9/dOwKKooZXcE+Yed\nSlFuQ7G/oqrxk8GrIKF/Qw==\n-----END PRIVATE KEY-----\n' # Ключ сервисного Google аккаунта
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