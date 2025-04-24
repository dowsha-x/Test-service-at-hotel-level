from django.db import models

from .constants import (LENGTH_DESCRIPTION, LENGTH_DECIMAL,
                        LENGTH_DIGITS, LENGTH_NAME)


class Rooms(models.Model):
    """
    Модель номера в гостиннице:

    desription - описание номера.
    price_per_night - стоимость номера за ночь.
    created_at - дата запуска номера.
    """
    description = models.TextField(
        'Описание номера', max_length=LENGTH_DESCRIPTION)
    price_per_night = models.DecimalField(
        'Стоимость за ночь', max_digits=LENGTH_DIGITS,
        decimal_places=LENGTH_DECIMAL)
    created_at = models.DateTimeField('Дата открытия', auto_now_add=True)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return f'Номер в отеле - {self.description[:100]}'


class Bookings(models.Model):
    """
    Модель бронирования номеров в гостиннице:

    room_id - id номера для привязки бронирования.
    date_start - дата заезда в номер.
    date_end - дата выезда из номера.
    guest_name - данные регистрируемого.
    created_at - дата создания брони.
    """
    room = models.ForeignKey(
        'Rooms', on_delete=models.CASCADE,
        related_name='bookings', verbose_name='Комната')
    date_start = models.DateField('Дата заезда')
    date_end = models.DateField('Дата выезда')
    guest_name = models.CharField('Имя гостя', max_length=LENGTH_NAME)
    created_at = models.DateTimeField('Дата создания брони', auto_now_add=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        # unique_together = ('room', 'date_start', 'date_end')
        ordering = ['date_start']

    def __str__(self):
        return (f'Бронирование для {self.guest_name} в {self.room.description}'
                f' с {self.date_start} по {self.date_end}')
