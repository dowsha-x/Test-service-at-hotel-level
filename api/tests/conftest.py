import pytest
from django.db import connection
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """API клиент для тестирования запросов."""
    return APIClient()


@pytest.fixture(scope='session')
def django_db_setup(django_db_blocker):
    """Создание временной таблицы для тестов."""
    with django_db_blocker.unblock():
        with connection.cursor() as cursor:
            with open('api/tests/test_table.sql', 'r') as f:
                sql = f.read()
                cursor.execute(sql)


@pytest.fixture
@pytest.mark.django_db
def room_1(api_client):
    data = {
        "description": "Комната 1",
        "price_per_night": "1000.00"
    }
    response = api_client.post("/rooms/create/", data, format='json')
    response._input_data = data
    return response


@pytest.fixture
@pytest.mark.django_db
def room_2(api_client):
    """Создание комнаты №2."""
    data = {
        "description": "Комната 2",
        "price_per_night": "5000.00"
    }
    return api_client.post("/rooms/create/", data, format='json')


@pytest.fixture
@pytest.mark.django_db
def rooms_response(api_client):
    """GET-запрос списка комнат."""
    url = "/rooms/"
    response = api_client.get(url)
    return response


@pytest.fixture
@pytest.mark.django_db
def room_3(api_client):
    """Создание комнаты для бронирования."""
    data = {
        "description": "Комната 1",
        "price_per_night": "1000.00"
    }
    response = api_client.post("/rooms/create/", data, format="json")
    room_id = response.data["id"]
    return room_id


@pytest.fixture
@pytest.mark.django_db
def booking_room_one(api_client, room_3):
    """Создание бронирования."""
    url = f"/bookings/{room_3}/create/"
    input_data = {
        "date_start": "2025-06-20",
        "date_end": "2025-06-25",
        "guest_name": "Иван Иванов"
    }
    response = api_client.post(url, data=input_data, format="json")
    response._input_data = input_data
    return response
