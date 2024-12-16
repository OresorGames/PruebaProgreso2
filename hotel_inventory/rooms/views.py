from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer

# Registrar nueva habitación
@api_view(['POST'])
def register_room(request):
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Actualizar el estado de una habitación
@api_view(['PATCH'])
def update_room_status(request, pk):
    try:
        room = Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        return Response({'error': 'Habitación no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    # Actualizar el estado de la habitación
    if 'status' in request.data:
        room.status = request.data['status']
        room.save()
        return Response({'message': f'Estado de la habitación {room.room_number} actualizado a {room.status}'}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Estado no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)
