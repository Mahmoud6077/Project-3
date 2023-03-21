from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# from django.db.models.signals import post_save
# from django.dispatch import receiver

#for Auth
# from django.contrib.auth.models import User
# Create your models here.
LOCATIONS = (
    ('m', 'Manama'),
    ('j', 'Jufair'),
    ('r', 'Riffa'),
    ('h', 'Hidd'),
    ('u', 'muharag'),
    ('i', 'Isa-Town')
)

class CustomUser(AbstractUser, models.Model):
    phone = models.IntegerField(default=0000)
    email = models.EmailField(max_length=100)
    # tickets = models.ForeignKey(Events, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    

class Events(models.Model):
    name = models.CharField(max_length = 150)
    location = models.CharField(max_length = 50, choices=LOCATIONS, default=LOCATIONS[0][0])
    description = models.TextField(max_length = 250)
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to ='main_app/static/images/', default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.name
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})
    

class Ticket(models.Model):
    User = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    ticket_number = models.IntegerField()