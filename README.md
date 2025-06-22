# 🏨 Hotel Booking Service

Простой сервис для управления номерами отелей и бронированиями.  
Реализован на Django + DRF с документацией Swagger и разворачивается через Docker.

---

## 🚀 Возможности

- 📋 Просмотр всех номеров
- ➕ Добавление и удаление номеров
- 🧾 Просмотр списка бронирований для конкретного номера
- 🏷️ Создание и удаление бронирований (если ещё не начались)
- 🔍 Swagger-документация по API

---

## ⚙️ Стек технологий

- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL
- drf-spectacular (Swagger)
- Docker / Docker Compose
- pre-commit + ruff
- pytest / pytest-django

---

## 📦 Установка и запуск

> 🔧 Перед запуском убедитесь, что у вас установлен Docker и файл `.env` в корне проекта.

### 📁 Пример `.env`:
```env
DB_NAME=hotel_db
DB_USER=postgres
DB_PASSWORD=postgres


### Сборка и запуск:

docker-compose up --build

Сервис будет доступен по адресу:
📍 http://localhost:8000

Документация Swagger:
📚 http://localhost:8000/swagger/


## API эндпоинты

Комнаты:

| Метод  | URL                        | Описание           |
| ------ | -------------------------- | ------------------ |
| GET    | `/rooms/`                  | Список всех комнат |
| POST   | `/rooms/create/`           | Создание комнаты   |
| DELETE | `/rooms/<room_id>/delete/` | Удаление комнаты   |

Бронирования:

| Метод  | URL                           | Описание                                 |
| ------ | ----------------------------- | ---------------------------------------- |
| GET    | `/bookings/<room_id>/`        | Список бронирований для комнаты          |
| POST   | `/bookings/<room_id>/create/` | Создание нового бронирования             |
| DELETE | `/bookings/<pk>/delete/`      | Удаление бронирования (если не началось) |


## Тестирование

Установи зависимости и запусти тесты:

pytest

## Структура проекта

.
├── api/                       # Views, serializers, urls
├── reservations/              # Модели номеров и бронирований
├── config/                    # Настройки Django
├── api/tests/test_service_at_hotel_level/  # Тесты
├── db/                        # SQL-дампы и init.sql
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env                       # Переменные окружения
