from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_planted = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plant-detail", kwargs={"plant_id": self.id})


class Watering(models.Model):
    date = models.DateField("Watering Date")

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"

    class Meta:
        ordering = ["-date"]
