from django.db import models
from django.urls import reverse
#for Auth
from django.contrib.auth.models import User
# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length = 150)
    location = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to ='main_app/static/images/', default="")
    def __str__(self):
        return self.name
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # def get_absolute_url(self):
    #     return reverse('toys_detail', kwargs={'pk': self.id})


