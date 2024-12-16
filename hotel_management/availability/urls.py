from django.urls import path
from .views import soap_availability

urlpatterns = [
    path('availability/', soap_availability, name='soap_availability'),
]
