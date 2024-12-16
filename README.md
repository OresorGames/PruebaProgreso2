# PruebaProgreso2
 
Diseñar e implementar una solución de integración que combine:
1. Un Servicio Web SOAP para manejar consultas de disponibilidad de
habitaciones.
2. Una API REST para realizar y cancelar reservas.
3. Un microservicio para gestionar las operaciones de actualización del inventario
de habitaciones.

# Sistema de Gestión Hotelera - Proyecto de Integración

Este proyecto implementa un sistema de gestión hotelera que incluye tres servicios independientes:
1. **Servicio Web SOAP** para consultar la disponibilidad de habitaciones.
2. **API REST** para realizar y cancelar reservas.
3. **Microservicio** para gestionar el inventario de habitaciones.

## Requisitos Previos

Antes de ejecutar los servicios, asegúrate de tener las siguientes herramientas instaladas:

- **Python 3.x**
- **Django 4.x o superior**
- **Django Rest Framework**
- **Zeep (para el servicio SOAP)**
- **Postman o cURL** para probar los servicios.

## Estructura del Proyecto

El proyecto contiene tres servicios independientes en carpetas separadas. Asegúrate de estar en la carpeta correcta cuando ejecutes los comandos para cada servicio.


---

## 1. **Servicio Web SOAP: Consultar Disponibilidad de Habitaciones**

### Pasos para ejecutar el servicio SOAP:

1. **Instalar dependencias**:
   En la carpeta `soap_service`, crea un entorno virtual e instala las dependencias necesarias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install django zeep

python manage.py makemigrations
python manage.py migrate


python manage.py runserver 8080

Usar postman para probar el servicio: 
<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <AvailabilityRequest xmlns="http://example.com/soap_service/">
            <start_date>2024-12-16</start_date>
            <end_date>2024-12-18</end_date>
            <room_type>Deluxe</room_type>
        </AvailabilityRequest>
    </soap:Body>
</soap:Envelope>


2. API REST: Gestión de Reservas
Pasos para ejecutar la API REST:
Instalar dependencias: En la carpeta reservation_service, crea un entorno virtual e instala las dependencias necesarias:

bash
Copy code
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install django djangorestframework
Configurar el proyecto: Asegúrate de que las migraciones se hayan realizado:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Ejecutar el servidor: Inicia el servidor Django:

bash
Copy code
python manage.py runserver
Probar los endpoints: Usa Postman o cURL para probar los siguientes endpoints:

Crear una reserva (Método: POST):

URL: http://localhost:8000/api/reservations/
Cuerpo en JSON:
json
Copy code
{
  "room_number": 101,
  "customer_name": "Juan Pérez",
  "start_date": "2024-12-16",
  "end_date": "2024-12-18",
  "status": "confirmed"
}
Consultar una reserva (Método: GET):

URL: http://localhost:8000/api/reservations/{id}/ (reemplaza {id} con el ID de la reserva)
Cancelar una reserva (Método: DELETE):

URL: http://localhost:8000/api/reservations/cancel/{id}/ (reemplaza {id} con el ID de la reserva)
3. Microservicio: Gestión de Inventario de Habitaciones
Pasos para ejecutar el microservicio:
Instalar dependencias: En la carpeta inventory_service, crea un entorno virtual e instala las dependencias necesarias:

bash
Copy code
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install django djangorestframework
Configurar el proyecto: Asegúrate de que las migraciones se hayan realizado:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Ejecutar el servidor: Inicia el servidor Django:

bash
Copy code
python manage.py runserver
Probar los endpoints: Usa Postman o cURL para probar los siguientes endpoints:

Registrar una nueva habitación (Método: POST):

URL: http://localhost:8000/api/rooms/
Cuerpo en JSON:
json
Copy code
{
  "room_number": 101,
  "room_type": "Deluxe",
  "status": "available"
}
Actualizar el estado de una habitación (Método: PATCH):

URL: http://localhost:8000/api/rooms/{id}/ (reemplaza {id} con el ID de la habitación)
Cuerpo en JSON:
json
Copy code
{
  "status": "maintenance"
}
Instrucciones Adicionales
Reiniciar el servidor: Si realizas cambios en el código de cualquier servicio, asegúrate de reiniciar el servidor para que se apliquen.
Pruebas: Cada servicio tiene endpoints para realizar pruebas. Usa Postman o cURL para enviar las solicitudes y validar las respuestas.
Base de Datos: Si necesitas agregar datos de prueba en la base de datos, puedes usar el python manage.py shell o los formularios del admin de Django.
