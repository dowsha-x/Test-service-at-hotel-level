# 🏨 Hotel Booking Service

Простой сервис для управления номерами отелей и бронированиями.  
Реализован на Django + DRF с документацией Swagger и разворачивается через Docker.

---

## 🚀 Возможности

- 📋 Просмотр всех номеров  
- ➕ Добавление и удаление номеров  
- 🧾 Просмотр списка бронирований для конкретного номера  
- 🏷️ Создание и удаление бронирований  
- 🔍 Swagger-документация по API  

---

## ⚙️ Стек технологий

- Python 3.9  
- Django 4.2  
- Django REST Framework  
- PostgreSQL  
- drf-spectacular (Swagger)  
- Docker / Docker Compose  

---

## 📦 Установка и запуск

1. Склонируйте репозиторий:
```bash
git clone https://github.com/your-repo/test-service-at-hotel-level.git
cd test-service-at-hotel-level

2. Создайте .env файл:

cp .env.example .env

И отредактируйте его:

DB_NAME=hotel_db
DB_USER=postgres
DB_PASSWORD=postgres
SECRET_KEY=ваш_секретный_ключ
DEBUG=True

3. Запустите сервис:

docker-compose up --build


---

## ⚙️ Стек технологий