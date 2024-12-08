# FastAPI Forms API

Этот проект — веб-приложение на FastAPI, которое позволяет работать с формами и их шаблонами. Пользователи могут
отправлять данные форм, а приложение проверяет, какие шаблоны им соответствуют, или возвращает предполагаемые типы
полей.

---

## Структура проекта

```plaintext
project/
├── app/
│   ├── __init__.py
│   ├── database.py          # Управление подключением к MongoDB
│   ├── main.py              # Основной файл приложения FastAPI
│   ├── validation.py        # Валидация полей форм
├── db/
│   ├── db_load.json         # Шаблоны форм для загрузки в MongoDB
│   ├── load_data.py         # Скрипт для загрузки шаблонов в базу данных
├── request_test/
│   ├── test_request.py      # Тестовые запросы к API
├── .dockerignore            # Исключения для сборки Docker-образа
├── docker-compose.yml       # Конфигурация сервисов (FastAPI + MongoDB)
├── Dockerfile               # Инструкция для создания Docker-образа
├── readme.md                # Документация проекта
├── requirements.txt         # Список зависимостей Python
├── run.sh                   # Скрипт для запуска приложения в Docker-контейнере
```

## Функциональность

### Роуты

1. **`GET /`**  
   Возвращает список всех шаблонов, доступных в базе данных.

2. **`POST /get_form`**  
   Проверяет, соответствует ли форма шаблону. Возвращает:
    - Имя подходящего шаблона, если он найден.
    - Предполагаемые типы полей, если шаблонов не найдено.

### Типы полей

- `date` — Дата (форматы: `YYYY-MM-DD`, `DD.MM.YYYY`).
- `tel` — Номер телефона (e.g., `+7 999 999 99 99`).
- `email` — Электронная почта (e.g., `example@mail.com`).
- `str` — Текст (строка).

## Установка и запуск

### 1. Локальный запуск

### Шаги:

1. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

2. Загрузите шаблоны в MongoDB:

    ```bash
    python -m db.load_data
    ```

3. Запустите сервер:
    ```bash
    python -m uvicorn app.main:app
    ```
4. Приложение будет доступно по адресу: http://127.0.0.1:8000.

### 2. Запуск через Docker
### Шаги:
1. Сборка и запуск контейнеров:
   ```bash
   docker compose up -d --build
   ```
2. Приложение будет доступно по адресу: http://localhost:8000.

### 3. Проверка API
### Тестовые запросы:
1. Убедитесь, что сервер работает.
2. Выполните тесты:
   ```bash
   python request_test/test_request.py
   ```

## Зависимости
- Python: 3.11
- FastAPI: 0.115.6
- MongoDB: 8.0.3
- Полный список зависимостей в файле `requirements.txt`.

## Лицензия
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



