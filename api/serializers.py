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
    date_start = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    date_end = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = Bookings
        fields = ("id", "date_start", "date_end", "guest_name", "created_at")

    def validate(self, data):
        room = self.context.get("room")
        if not room:
            raise serializers.ValidationError("Комната не указана.")

        date_start = data.get("date_start")
        date_end = data.get("date_end")

        if not date_start or not date_end:
            raise serializers.ValidationError("Обе даты обязательны.")

        if date_start >= date_end:
            raise serializers.ValidationError("Дата заезда должна быть раньше даты выезда.")

        if Bookings.objects.filter(
            room=room,
            date_start__lt=date_end,
            date_end__gt=date_start,
        ).exists():
            raise serializers.ValidationError("Комната уже забронирована на эти даты.")

        return data

    def create(self, validated_data):
        room = self.context.get("room")
        return Bookings.objects.create(room=room, **validated_data)
