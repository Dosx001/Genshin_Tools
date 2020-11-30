from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Task
from .forms import TaskForm

class TaskView(View):
    def get(self, request):
        form = TaskForm()
        events = Task.objects.all()
        context = {
            'form': form,
            'events': events,
        }
        return render(request, 'task/task.html', context)

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            new_event = form.save()
            return JsonResponse({'event':model_to_dict(new_event)}, status=200)
        else:
            return redirect('task')
