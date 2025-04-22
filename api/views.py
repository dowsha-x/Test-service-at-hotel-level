from datetime import datetime

from rest_framework import status, generics, filters
from rest_framework.response import Response

from .serializers import BookingsSerializer, RoomsSerializer
from reservations.models import Bookings, Rooms


class BookingsCreateDeleteListView(
    generics.CreateAPIView, generics.DestroyAPIView, generics.ListAPIView
):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date_start']

    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room_id')
        date_start = request.data.get('date_start')
        date_end = request.data.get('date_end')

        if not room_id:
            return Response({"error": "ID комнаты не указан"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            room = Rooms.objects.get(id=room_id)
        except Rooms.DoesNotExist:
            return Response({"error": f"Комната с ID {room_id} не существует."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            date_start = datetime.strptime(date_start, "%Y-%m-%d").date()
            date_end = datetime.strptime(date_end, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "Неверный формат даты. Даты должны быть в формате YYYY-MM-DD."},
                            status=status.HTTP_400_BAD_REQUEST)

        if date_start >= date_end:
            return Response({"error": "Дата заезда не может быть позже даты выезда."},
                            status=status.HTTP_400_BAD_REQUEST)

        request.data['room_id'] = room.id

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            booking = serializer.save()
            return Response({"id": booking.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Bookings.objects.filter(
            room_id=room_id).order_by(*self.ordering)


class RoomsCreateDeleteListView(generics.CreateAPIView,
                                generics.DestroyAPIView, generics.ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['created_at', 'price_per_night']
