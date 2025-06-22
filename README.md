# 🏨 Hotel Booking API Service

![Django](https://img.shields.io/badge/Django-4.2-brightgreen)
![DRF](https://img.shields.io/badge/DRF-3.14-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue)

Микросервис для управления бронированием номеров отеля с REST API интерфейсом.

## 🚀 Быстрый запуск

### Требования
- Docker и Docker Compose
- Python 3.9+

```bash
git clone https://github.com/your-repo/hotel-booking-api.git
cd hotel-booking-api
cp .env.example .env
```

#### Заполните .env файл:

```ini
DB_NAME=hotel_db
DB_USER=postgres
DB_PASSWORD=your_password
SECRET_KEY=your_secret_key
DEBUG=True
```

### Запустите сервис:

```bash
docker-compose up --build
```

## 🚀 API Documentation

### Доступные интерфейсы:

```bash
Swagger UI: http://localhost:8000/swagger/

ReDoc: http://localhost:8000/redoc/
```

### Основные endpoints:

#### Управление номерами

Комнаты:
| Метод  | URL                        | Описание           |
| ------ | -------------------------- | ------------------ |
| GET    | `/rooms/`                  | Список всех комнат |
| POST   | `/rooms/create/`           | Создание комнаты   |
| DELETE | `/rooms/<room_id>/delete/` | Удаление комнаты   |

Управление бронированиями:
| Метод  | URL                           | Описание                                 |
| ------ | ----------------------------- | ---------------------------------------- |
| GET    | `/bookings/<room_id>/`        | Список бронирований для комнаты          |
| POST   | `/bookings/<room_id>/create/` | Создание нового бронирования             |
| DELETE | `/bookings/<pk>/delete/`      | Удаление бронирования (если не началось) |

#### Примеры запросов
Создание номера
```bash
curl -X POST "http://localhost:8000/rooms/create/" \
-H "Content-Type: application/json" \
-d '{"description": "Deluxe Suite", "price_per_night": 15000}'
```
#### Создание бронирования
```bash
curl -X POST "http://localhost:8000/bookings/1/create/" \
-H "Content-Type: application/json" \
-d '{"date_start": "2025-07-01", "date_end": "2025-07-05"}'
```

## Тестирование

Установи зависимости и запусти тесты:

```bash
pytest
```

## Технические детали

* PostgreSQL

* Django ORM для работы с БД

* DRF для построения API

* Автоматическая документация через drf-spectacular
