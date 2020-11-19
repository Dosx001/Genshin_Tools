from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pity_counter-home'),
]
