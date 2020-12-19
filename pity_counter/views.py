from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import JsonResponse

from users.models import Profile

class PityCounterView(View):
    def get(self, request):
        context = {
            'profile': Profile() if request.user.is_anonymous else request.user.profile
        }
        return render(request, 'pity_counter/pity_counter.html', context)

    def post(self, request):
        if request.user.is_anonymous:
            return redirect('pity_counter')
        pity = request.POST.get('id', None)
        value = request.POST.get('value', None)
        if pity == 'Char':
            if value == 'reset':
                request.user.profile.character = 0
            else:
                request.user.profile.character += int(value)
            check = request.user.profile.character
        elif pity == 'Weap':
            if value == 'reset':
                request.user.profile.weapon = 0
            else:
                request.user.profile.weapon += int(value)
            check = request.user.profile.weapon
        else:
            if value == 'reset':
                request.user.profile.standard = 0
            else:
                request.user.profile.standard += int(value)
            check = request.user.profile.standard
        if pity == 'Char' and check >= 90:
            request.user.profile.character = 0
        elif pity == 'Weap' and check >= 80:
            request.user.profile.weapon = 0
        elif pity == 'Stan' and check >= 90:
            request.user.profile.standard = 0
        request.user.profile.save()
        return redirect('pity_counter')

class BlessingView(View):
    def post(self, request):
        request.user.profile.blessing = not request.user.profile.blessing
        request.user.save()
        return redirect('pity_counter')

class ReportView(View):
    def post(self, request):
        primogems = int(request.POST.get('primogems', None))
        pity = 90 - request.user.profile.character
        primo = pity * 160 - primogems
        days = round(primo / 150 if request.user.profile.blessing else primo / 60, 1)
        context = {
            'primo': primo,
            'days': days
            }
        return JsonResponse(context)
