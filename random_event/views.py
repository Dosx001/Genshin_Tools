from django.shortcuts import render
from django.views.generic import View

class RandomEventView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'random_event.html', context)
