from django.contrib import admin
from .models import Events, CustomUser, Ticket

# Register your models here.
admin.site.register(Events)
admin.site.register(CustomUser)
admin.site.register(Ticket)

