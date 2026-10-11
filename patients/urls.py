from django.urls import path,include

from .import views

urlpatterns = [
    path('', views.patient, name='patient'),
]