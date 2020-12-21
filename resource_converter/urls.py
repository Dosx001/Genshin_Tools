from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('resource_converter/', ResourceConverterView.as_view(), name='resource_converter'),
]
