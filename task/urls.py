from django.urls import path
from .views import TaskView, TaskComplete

urlpatterns = [
    path('task/', TaskView.as_view(), name='task'),
    path('task/<str:id>/completed/', TaskComplete.as_view(), name='task_complete'),
]
