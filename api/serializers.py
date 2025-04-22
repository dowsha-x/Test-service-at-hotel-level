from rest_framework import serializers

from reservations.models import Rooms, Bookings


class RoomsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Rooms.
    Отвечает за преобразование данных модели в JSON и обратно.
    """
    class Meta:
        fields = ('id', 'description', 'price_per_night', 'created_at')
        model = Rooms

    def validate_price_per_night(self, value):
        """
        Проверка, чтобы цена за ночь была больше 0.
        """
        if value <= 0:
            raise serializers.ValidationError(
                'Стоимость за ночь должна быть больше нуля.')
        return value


class BookingsSerializer(serializers.ModelSerializer):
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Rooms.objects.all())

    class Meta:
        model = Bookings
        fields = ('id', 'room_id', 'date_start',
                  'date_end', 'guest_name', 'created_at')

    def validate(self, data):
        """
        Проверяем, что бронирование не пересекается с уже существующим.
        Отвечает за преобразование данных модели в JSON и обратно.
        """
        room_id = data.get('room_id')
        date_start = data.get('date_start')
        date_end = data.get('date_end')

        overlapping_bookings = Bookings.objects.filter(
            room_id=room_id,
            date_start__lt=date_end,
            date_end__gt=date_start)

        if overlapping_bookings.exists():
            room = room_id
            raise serializers.ValidationError(
                f'Комната "{room.description}" уже забронирована на эти даты.')
        return data
