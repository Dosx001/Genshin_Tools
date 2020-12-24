from django.shortcuts import render, redirect
from django.views.generic import View
import json

class ResourceConverterView(View):
    def get(self, request):
        return render(request, 'resource_converter.html')

    def post(self, request):
        data = json.loads(request.POST.get('data', None))
        print(data)
        activity = request.POST.get('activity', None)
        if activity == 'Domain of Mastery':
            print('test')
        return redirect('resource_converter')

    def mastery(self, adv_rank, data):
        if adv_rank == 27:
            rates = ((1, 3))
        elif 27 < adv_rank < 36:
            rates = ((1, 3), (1, 2))
        elif 35 < adv_rank < 45:
            rates = ((1, 3), (1, 3))
        elif 44 < adv_rank:
            rates = ((2, 3), (0, 3), (0, 2))
        else:
            return

    def forgery(self, adv_rank, data):
        if 15 < adv_rank < 21:
            rates = ((4, 6))
        elif 20 < adv_rank < 30:
            rates = ((2, 3), (1, 3))
        elif 29 < adv_rank < 40:
            rates = ((0, 3), (1, 3), (0, 2))
        elif 39 < adv_rank:
            rates = ((2, 3), (0, 4), (0, 3), (0, 1))
        else:
            return

    def boss(self, adv_rank, data):
        if adv_rank < 20:
            rates = ((1, 3))
        elif 19 < adv_rank < 25:
            rates = ((1, 3), (1, 2))
        elif 24 < adv_rank < 30:
            rates = ((1, 3), (1, 3))
        elif 29 < adv_rank < 35:
            rates = ((2, 3), (0, 3), (0, 2))
        elif 34 < adv_rank < 40:
            rates = ((2, 3), (0, 3), (0, 2))
        elif 39 < adv_rank < 45:
            rates = ((2, 3), (0, 3), (0, 2))
        elif 44 < adv_rank < 50:
            rates = ((2, 3), (0, 3), (0, 2))
        elif 49 < adv_rank < 55:
            rates = ((2, 3), (0, 3), (0, 2))
        elif 54 < adv_rank < 61:
            rates = ((2, 3), (0, 3), (0, 2))
        else:
            return
