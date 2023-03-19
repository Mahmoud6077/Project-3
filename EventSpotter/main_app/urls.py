from django.contrib import admin
from . import views
# Add the include function to the import
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # In this case '' represents the root route
    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    # path('about/', views.about, name='about'),
    path('accounts/signup', views.signup, name='signup')


]