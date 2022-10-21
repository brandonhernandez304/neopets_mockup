from django.db import models
from django.urls import reverse

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={pk: self.id})
        
class Neopet(models.Model):
    name = models.CharField(max_length=30)
    species = models.CharField(max_length = 20)
    gender = models.CharField(max_length=20)
    temperament = models.CharField(max_length=30)
    # M:M
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'neopet_id': self.id})
