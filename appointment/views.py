from django.shortcuts import render

# Create your views here.

def appointment(req):
    return render(req, 'appointment.html')

def schedule(req):
    return render(req, 'schedule.html')

def appointment_list(req):
    return render(req, 'appointment_list.html')