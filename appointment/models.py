from django.db import models

# Create your models here.


class Appointment(models.Model):
    fullname = models.CharField(max_length=100)
    appoint_name = models.CharField(max_length=100)
    time_in = models.TimeField()
    time_out = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return f"{self.fullname} - {self.appoint_name}"