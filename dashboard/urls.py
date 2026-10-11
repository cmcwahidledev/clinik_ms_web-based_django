from django.urls import path,include
from django.views.generic import TemplateView as template_name

from .import views

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
]