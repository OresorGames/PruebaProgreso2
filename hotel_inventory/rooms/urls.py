from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.register_room, name='register_room'),
    path('rooms/<int:pk>/', views.update_room_status, name='update_room_status'),
]
