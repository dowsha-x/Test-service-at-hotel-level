from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BookingsCreateDeleteListView, RoomsCreateDeleteListView


router = DefaultRouter()
router.register(r'bookings', BookingsCreateDeleteListView, basename='booking')
router.register(r'rooms', RoomsCreateDeleteListView, basename='room')

urlpatterns = [
    path('bookings/<int:room_id>/',
         BookingsCreateDeleteListView.as_view(), name='booking-list'),
    path('bookings/<int:room_id>/create/',
         BookingsCreateDeleteListView.as_view(), name='booking-create'),
    path('bookings/<int:room_id>/delete/<int:pk>/',
         BookingsCreateDeleteListView.as_view(), name='booking-delete'),
    path('rooms/',
         RoomsCreateDeleteListView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/',
         RoomsCreateDeleteListView.as_view(), name='room-delete'),
]

urlpatterns += router.urls
