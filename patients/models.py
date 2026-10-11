from django.db import models

# Create your models here.

class Patient(models.Model):
    fullname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

def __str__(self):
    return self.fullname