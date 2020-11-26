from django.urls import path
from . import views
from .views import PityCounterView

urlpatterns = [
    path('pity_counter/', PityCounterView.as_view(), name='pity_counter'),
]
