from django.shortcuts import render
from django.views.generic import View
import json

class QuestLogView(View):
    def get(self, request):
        with open('quest_log/missions.json') as f:
            data = json.load(f)
        context = {
            'Archon': data['Archon'],
            'World': data['World'],
            'Commission': data['Commission']
        }
        return render(request, 'quest_log.html', context)
