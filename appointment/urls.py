from django.urls import path,include
from django.views.generic import TemplateView as template_name

from .import views

urlpatterns = [
    path('',views.appointment, name='appointment'),
    path('schedule/',views.schedule, name='schedule'),
    path('appointment_list/',views.appointment_list, name='appointment_list'),
]