from django.urls import path

from .views import (
    BookingCreateView,
    BookingsListView,
    BookingsDeleteView,
    RoomListView,
    RoomCreateView,
    RoomDeleteView
)

urlpatterns = [
    path('rooms/',
         RoomListView.as_view(), name='room-list'),
    path('rooms/create/',
         RoomCreateView.as_view(), name='room-create'),
    path('rooms/<int:room_id>/delete/',
         RoomDeleteView.as_view(), name='room-delete'),

    path('bookings/<int:room_id>/',
         BookingsListView.as_view(), name='booking-list'),
    path('bookings/',
         BookingCreateView.as_view(), name='booking-create'),
    path('bookings/<int:room_id>/delete/',
         BookingsDeleteView.as_view(), name='booking-delete'),
]
