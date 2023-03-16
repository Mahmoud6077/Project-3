from django.db import models
from django.urls import reverse
# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length = 150)
    location = models.CharField(max_length = 100)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse('toys_detail', kwargs={'pk': self.id})


