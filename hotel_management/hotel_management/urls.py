from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('soap/', include('availability.urls')),  # Asegúrate de que esto esté configurado correctamente
]
