from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_planted = models.DateField()

    def __str__(self):
        return self.name