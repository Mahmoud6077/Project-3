from django.db import models
from django.urls import reverse
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import UserProfile
#for Auth
from django.contrib.auth.models import User
# Create your models here.
LOCATIONS = (
    ('m', 'Manama'),
    ('j', 'Jufair'),
    ('r', 'Riffa'),
    ('h', 'Hidd'),
    ('u', 'muharag'),
    ('i', 'Isa-Town')
)

class Events(models.Model):
    name = models.CharField(max_length = 150)
    location = models.CharField(max_length = 1, choices=LOCATIONS, default=LOCATIONS[0][0])
    description = models.TextField(max_length = 250)
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to ='main_app/static/images/', default="")
    # def __str__(self):
    #     return self.name
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'event_id': self.id})
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    