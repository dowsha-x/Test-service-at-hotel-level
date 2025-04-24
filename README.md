# Test-service-at-hotel-level
Простой сервис для управления номерами отелей и бронированиями.

Для начала работы выполни эти пункты:

## Установка зависимостей

poetry add $(cat requirements.txt)

## Активация виртуального окружения

poetry env activate

Затем активируйте виртуальное окружение командой source, используя путь, выданный Poetry:

source /путь/к/виртуальному/окружению/bin/activate

## Примените миграции

Примените миграции:

python manage.py migrate

## Запуск проекта

python manage.py runserver

Это запустит сервер на http://127.0.0.1:8000/ (по умолчанию), и вы сможете обратиться к вашему приложению через веб-браузер.

## Доступ к документации API

Интерфейс Swagger UI доступен по следующему URL в вашем браузере:

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

Вы можете получить доступ к Redoc, перейдя по следующему URL:

- **Redoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
