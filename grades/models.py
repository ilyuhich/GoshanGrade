from django.db import models


# Create your models here.

class Quarters(models.Model):
    """records for class and quarter"""
    year = models.SmallIntegerField(verbose_name='Год обучения')
    quarter = models.SmallIntegerField(verbose_name='Четверть')

    def __str__(self):
        return 'Класс: ' + str(self.year) + ', четверть: ' + str(self.quarter)

    class Meta:
        verbose_name = 'Четверть'
        verbose_name_plural = 'Четверти'


class Subjects(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
