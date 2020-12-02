from django.urls import path
from .views import *

urlpatterns = [
    path('random_event/', RandomEventView.as_view(), name='random_event'),
]
