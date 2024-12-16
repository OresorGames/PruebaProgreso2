from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rooms.urls')),  # Agregar la ruta para la API de habitaciones
]
