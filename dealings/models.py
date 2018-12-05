from django.db import models

# Create your models here.
class visualization(models.Model):
    name = models.CharField(max_length=100)
    money = models.FloatField(default=0)
    day = models.DateField()

    def __str__(self):
        return '<Money_name:id=' + str(self.id) + ',' + self.name + str(money)
