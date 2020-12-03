from django.shortcuts import render
from django.views.generic import View

class QuestLogView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'quest_log.html', context)
