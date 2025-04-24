from django.http import Http404
from django.utils import timezone
from rest_framework import status, generics, filters
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .serializers import BookingsSerializer, RoomsSerializer
from reservations.models import Bookings, Rooms


class RoomListView(generics.ListAPIView):
    """
    Список всех комнат
    GET /rooms/
    """
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at', 'price_per_night']
    ordering = ['created_at']


class RoomCreateView(generics.CreateAPIView):
    """
    Создание комнаты
    POST /rooms/
    """
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        room = serializer.save()
        return Response({"id": room.id}, status=status.HTTP_201_CREATED)


class RoomDeleteView(generics.DestroyAPIView):
    """
    Удаление комнаты
    DELETE /rooms/<pk>/
    """
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'room_id'

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            raise NotFound(
                detail=f"Комната с ID {kwargs.get('room_id')} не найдена."
            )
        room_id = instance.id
        self.perform_destroy(instance)
        return Response(
            {"detail": f"Комната с ID {room_id} и все её бронирования удалены."},
            status=status.HTTP_200_OK
        )


class BookingCreateView(generics.CreateAPIView):
    """
    Создание бронирования для комнаты
    POST /bookings/<room_id>/create/
    """
    serializer_class = BookingsSerializer

    def create(self, request, *args, **kwargs):
        room_id = kwargs.get('room_id')
        try:
            room = Rooms.objects.get(id=room_id)
        except Rooms.DoesNotExist:
            return Response(
                {"error": f"Комната с ID {room_id} не существует."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.data['room'] = room.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()

        return Response(
            {"id": booking.id},
            status=status.HTTP_201_CREATED
        )


class BookingsListView(generics.ListAPIView):
    """
    Список бронирований для комнаты
    GET /bookings/<room_id>/
    """
    serializer_class = BookingsSerializer
    ordering = ['date_start']

    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        return Bookings.objects.filter(room_id=room_id).select_related('room')


class BookingsDeleteView(generics.DestroyAPIView):
    """
    Удаление бронирования
    DELETE /bookings/<pk>/
    """
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        try:
            booking = self.get_object()
        except Http404:
            raise NotFound(
                detail=f"Бронирование с ID {kwargs.get('pk')} не найдено."
            )

        if booking.date_start < timezone.now().date():
            return Response(
                {"error": "Нельзя удалить начавшееся бронирование"},
                status=status.HTTP_400_BAD_REQUEST
            )

        booking.delete()
        return Response(
            {"message": f"Бронирование {kwargs['pk']} удалено"},
            status=status.HTTP_200_OK
        )
