from django.db import models

class Reservation(models.Model):
    room_number = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='confirmed')

    def __str__(self):
        return f"Reservation {self.id} - {self.customer_name}"