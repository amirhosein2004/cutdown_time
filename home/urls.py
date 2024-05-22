from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('countdown_timer/<str:pk_event>', views.countdown_timer, name='countdown_timer'),
    path('create_event', views.create_event, name='create_event'),
    path('edit_event/<str:pk_event>', views.edit_event, name='edit_event'),
    path('remove/<str:pk_event>', views.remove_event, name='remove_event'),
]