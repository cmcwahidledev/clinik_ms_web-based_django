from django.shortcuts import render
from.models import Patient
# Create your views here.

def patient(request):
    patients = Patient.objects.all()
    return render(request, 'patient.html', {'patients': patients})