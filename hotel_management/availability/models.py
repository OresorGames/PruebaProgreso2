from django.db import models

class RoomAvailability(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_type = models.CharField(max_length=50)
    available_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('booked', 'Booked')])

    def __str__(self):
        return f"{self.room_type} - {self.status} ({self.available_date})"
