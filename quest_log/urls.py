from django.urls import path
from .views import *

urlpatterns = [
    path('quest_log/', QuestLogView.as_view(), name='quest_log'),
]
