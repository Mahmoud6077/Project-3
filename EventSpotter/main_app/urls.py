from django.contrib import admin
from . import views
# Add the include function to the import
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # In this case '' represents the root route
    path('', views.home, name='home') ,     # equivalent to route.get('/', homeController.home_get)
    path('about/', views.about, name='about'),
    path('events/', views.events_index, name='index') ,
    path('events/<int:event_id>', views.events_detail, name='detail'),
    path('accounts/signup', views.signup, name='signup'),
    path('profile/', views.profile, name="profile"),
    path('events/create',views.EventCreate.as_view(), name='events_create'),
    path('events/<int:pk>/update', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete', views.EventDelete.as_view(), name='events_delete'),
    path('events/<int:event_id>/booking', views.EventBooking, name='events_booking'),
    path('events/<int:event_id>/booking/booking_successfull', views.booking_success, name='booking_success'),


]