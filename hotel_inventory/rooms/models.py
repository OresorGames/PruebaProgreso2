from django.db import models

class Room(models.Model):
    room_number = models.IntegerField(unique=True)
    room_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('booked', 'Booked'), ('maintenance', 'Maintenance')], default='available')

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type} ({self.status})"
