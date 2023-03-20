from django.contrib import admin
from . import views
# Add the include function to the import
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # In this case '' represents the root route
    path('', views.home, name='home') ,     # equivalent to route.get('/', homeController.home_get)
    path('events/', views.events_index, name='index') ,
    path('events/<int:event_id>', views.events_detail, name='detail'),
    path('accounts/signup', views.signup, name='signup'),
    path('profile/', views.profile, name="profile")

]