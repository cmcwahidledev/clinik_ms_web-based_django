from django.shortcuts import render

# Create your views here.

def doctor(req):
    return render(req, 'doctor.html')