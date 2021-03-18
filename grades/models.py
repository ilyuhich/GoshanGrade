from django.db import models


# Create your models here.

class Quarter(models.Model):
    """records for class and quarter"""
    year = models.SmallIntegerField(verbose_name='Год обучения')
    quarter = models.SmallIntegerField(verbose_name='Четверть')

    def __str__(self):
        return 'Класс: ' + str(self.year) + ', четверть: ' + str(self.quarter)

    class Meta:
        verbose_name = 'Четверть'
        verbose_name_plural = 'Четверти'
