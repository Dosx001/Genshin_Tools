from django.urls import path, include
from . import views
from pity_counter import views as pity_views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('pity_counter/', pity_views.home, name='pity_counter'),
]
