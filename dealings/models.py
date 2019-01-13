from django.db import models

# Create your models here.
class Visualization(models.Model):
    choice_name = (
        ('消費','消費'),
        ('無駄使い', '無駄使い'),
        ('投資','投資')
    )
    name = models.CharField(max_length=100, choices=choice_name, default=0)
    money = models.FloatField(default=0)
    day = models.DateField(verbose_name='日付',blank=True,null=True)

    def __str__(self):
        return self.name + ':' + str(self.money) + '：' + str(self.day)

class Income_visualization(models.Model):
    income_name = (
        ('固定収入','固定収入'),
        ('変動収入', '変動収入')
    )
    name = models.CharField(choices=income_name, max_length=100, default=0)
    income = models.FloatField(default=0)

    def __str__(self):
        return self.name + ':' + str(self.income)
