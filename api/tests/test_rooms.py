from datetime import datetime

import pytest


@pytest.mark.django_db
def test_create_and_list_room(room_1, rooms_response):
    """Тестирование создания комнаты и её наличия в списке."""
    assert room_1.status_code == 201

    input_data = getattr(room_1, "_input_data", {})

    assert any(
        room["id"] == room_1.data["id"]
        and room["description"] == input_data.get("description")
        and room["price_per_night"] == input_data.get("price_per_night")
        for room in rooms_response.data
    )


@pytest.mark.django_db
def test_ordering_rooms(room_1, room_2, rooms_response):
    """Тестирование сортировки комнат по возрастанию."""
    room1 = next(
        r for r in rooms_response.data if r["id"] == room_1.data["id"]
    )
    room2 = next(
        r for r in rooms_response.data if r["id"] == room_2.data["id"]
    )

    created1 = datetime.fromisoformat(
        room1["created_at"].replace("Z", "+00:00")
    )
    created2 = datetime.fromisoformat(
        room2["created_at"].replace("Z", "+00:00")
    )

    assert created2 > created1


@pytest.mark.django_db
def test_delete_room(api_client, room_1):
    """Тестирование на удаление комнаты."""
    room_id = room_1.data["id"]

    delete_url = f"/rooms/{room_id}/delete/"
    delete_response = api_client.delete(delete_url)
    assert delete_response.status_code == 200

    list_response = api_client.get("/rooms/")
    assert all(room["id"] != room_id for room in list_response.data)
