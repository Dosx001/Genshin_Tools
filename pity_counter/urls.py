from django.urls import path
from . import views

urlpatterns = [
    path('pity_counter/', views.home, name='pity_counter'),
]
