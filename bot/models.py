from django.db import models


class Bouquet(models.Model):
    name = models.CharField('Название букета:', max_length=100)
    description = models.TextField('Описание и состав букета:', blank=True)
    price = models.IntegerField('Цена в Р:')
    photo = models.ImageField('Фото букета:', upload_to='bouquets/', blank=True, null=True)
    is_available = models.BooleanField('В продаже:', default=True)
    created_at = models.DateTimeField('Дата добавления букета:', auto_now_add=True)
    updated_at = models.DateTimeField('Дата последнего изменения:', auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.price}₽)"
