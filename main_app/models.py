from django.db import models
from django.urls import reverse

# Create your models here.
class Neopet(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length = 20)
    gender = models.CharField(max_length=20)
    temperament = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'neopet_id': self.id})