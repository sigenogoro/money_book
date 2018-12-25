from django.db import models

# Create your models here.
class Visualization(models.Model):
    choice_name = (
        ('消費','消費'),
        ('浪費', '浪費'),
        ('投資','投資')
    )
    name = models.CharField(max_length=100, choices=choice_name, default=0)
    money = models.FloatField(default=0)
    day = models.DateField(verbose_name='日付',blank=True,null=True)

    def __str__(self):
        return self.name + ':' + str(self.money) + '：' + str(self.day)

