import xml.etree.ElementTree as ET
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RoomAvailability

@csrf_exempt
def soap_availability(request):
    if request.method == 'POST':
        try:
            # Parsear el XML recibido
            tree = ET.ElementTree(ET.fromstring(request.body))
            root = tree.getroot()

            # Extraer datos de la solicitud
            namespace = {'ns': 'http://example.com/soap_service/'}
            start_date = root.find('.//ns:start_date', namespace).text
            end_date = root.find('.//ns:end_date', namespace).text
            room_type = root.find('.//ns:room_type', namespace).text

            # Consultar la base de datos
            available_rooms = RoomAvailability.objects.filter(
                room_type=room_type,
                available_date__range=(start_date, end_date),
                status="available"
            )

            # Crear la respuesta en XML
            response = ET.Element("AvailabilityResponse")
            rooms = ET.SubElement(response, "rooms")
            for room in available_rooms:
                room_element = ET.SubElement(rooms, "room")
                room_element.text = str(room.room_id)

            # Convertir el árbol XML a cadena
            response_xml = ET.tostring(response, encoding="unicode")
            return HttpResponse(response_xml, content_type="application/xml")

        except Exception as e:
            error_response = f"<Error>{str(e)}</Error>"
            return HttpResponse(error_response, content_type="application/xml")
    return HttpResponse("Invalid Request", status=400)
