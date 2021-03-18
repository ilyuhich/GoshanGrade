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


class Grades(models.Model):
    grade_date = models.DateField(verbose_name='Дата')
    grade_quarter = models.ForeignKey('Quarters', on_delete=models.PROTECT, verbose_name='четверть')
    grade_subject = models.ForeignKey('Subjects', on_delete=models.PROTECT, verbose_name='предмет')
    grade = models.SmallIntegerField(verbose_name='оценка')

    def __str__(self):
        return str(self.grade_date) + ' ' + self.grade_subject.name + ' ' + str(self.grade)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
