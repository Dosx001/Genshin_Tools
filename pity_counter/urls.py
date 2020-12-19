from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('pity_counter/', PityCounterView.as_view(), name='pity_counter'),
    path('pity_counter/blessing/', BlessingView.as_view(), name='blessing'),
    path('pity_counter/report/', ReportView.as_view(), name='report'),
]
