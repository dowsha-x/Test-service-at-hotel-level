import pytest


@pytest.mark.django_db
def test_create_and_list_id_booking(api_client, room_3, booking_room_one):
    """Тестирование создания бронирования для комнаты."""
    assert booking_room_one.status_code == 201

    input_data = getattr(booking_room_one, "_input_data", {})
    booking_data = booking_room_one.data
    assert booking_data["date_start"] == input_data.get("date_start")
    assert booking_data["date_end"] == input_data.get("date_end")
    assert booking_data["guest_name"] == input_data.get("guest_name")
    assert "id" in booking_data


@pytest.mark.django_db
def test_delete_booking(api_client, booking_room_one, room_3):
    booking_id = booking_room_one.data["id"]

    delete_url = f"/bookings/{booking_id}/delete/"
    delete_response = api_client.delete(delete_url)
    assert delete_response.status_code == 204

    list_url = f"/bookings/{room_3}/"
    list_response = api_client.get(list_url)
    assert list_response.status_code == 200

    returned_ids = [booking["id"] for booking in list_response.data]
    assert booking_id not in returned_ids


@pytest.mark.django_db
def test_booking_overlapping_dates(api_client, room_3):
    """Тестирование на совпадающие даты бронирования."""
    first_booking = {
        "date_start": "2025-06-21",
        "date_end": "2025-06-23",
        "guest_name": "Первый гость"
    }
    create_url = f"/bookings/{room_3}/create/"
    response1 = api_client.post(create_url, data=first_booking, format="json")
    assert response1.status_code == 201

    second_booking = {
        "date_start": "2025-06-22",
        "date_end": "2025-06-24",
        "guest_name": "Второй гость"
    }
    response2 = api_client.post(create_url, data=second_booking, format="json")

    assert response2.status_code == 400
    assert "Комната уже забронирована на эти даты" in str(response2.data)
