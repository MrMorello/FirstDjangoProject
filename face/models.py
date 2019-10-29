from django.db import models


class Order(models.Model):
    date = models.DateField(verbose_name='Дата вывоза')
    subdivision = models.CharField(max_length=50, verbose_name='Подразделение')
    reason = models.CharField(max_length=50, verbose_name='Причина')
    where = models.CharField(max_length=50, verbose_name='Куда')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Products(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Наименование')
    price = models.FloatField(verbose_name='Цена')
    quantity = models.FloatField(verbose_name='Количество')

    PIECES = 'шт'
    KILOGRAMMS = 'кг'
    METERS = 'м'
    KOMPLEKT = 'кт'
    MEASUREMENTS = (
        (PIECES, 'шт'),
        (KILOGRAMMS, 'кг'),
        (METERS, 'м'),
        (KOMPLEKT, 'кт'),
    )
    measurement = models.CharField(
        max_length=2,
        choices=MEASUREMENTS,
        default=PIECES, verbose_name='ед. изм'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def is_upperclass(self):
        return self.measurement in (self.PIECES, self.KOMPLEKT)

    def __str__(self):
        return self.name
