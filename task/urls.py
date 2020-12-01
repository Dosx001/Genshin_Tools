from django.urls import path
from .views import *

urlpatterns = [
    path('task/', TaskView.as_view(), name='task'),
    path('task/<str:id>/completed/', TaskComplete.as_view(), name='task_complete'),
    path('task/<str:id>/delete/', TaskDelete.as_view(), name='task_delete'),
]
