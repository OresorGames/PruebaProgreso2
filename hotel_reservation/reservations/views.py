from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer

# Crear reserva
@api_view(['POST'])
def create_reservation(request):
    if request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Consultar reserva
@api_view(['GET'])
def get_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response({'error': 'Reserva no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)

# Cancelar reserva
@api_view(['DELETE'])
def cancel_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response({'error': 'Reserva no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    reservation.status = 'cancelled'
    reservation.save()
    return Response({'message': 'Reserva cancelada'}, status=status.HTTP_204_NO_CONTENT)
