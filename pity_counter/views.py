from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import JsonResponse
from datetime import date
import datetime

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
            if request.user.profile.character >= 90:
                request.user.profile.character = 0
        elif pity == 'Weap':
            if value == 'reset':
                request.user.profile.weapon = 0
            else:
                request.user.profile.weapon += int(value)
            if request.user.profile.weapon >= 80:
                request.user.profile.weapon = 0
        else:
            if value == 'reset':
                request.user.profile.standard = 0
            else:
                request.user.profile.standard += int(value)
            if request.user.profile.standard >= 90:
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
        primo = self.Primo(request)
        price = self.price(request, primo)
        days, Date = self.Date(request, primo)
        context = {
            'primo': primo,
            'days': days,
            'date': Date,
            'price': price
            }
        return JsonResponse(context)

    def Primo(self, request):
        primogems = int(request.POST.get('primogems', None))
        banner = request.POST.get('banner', None)
        if banner == 'Char':
            pity = 90 - request.user.profile.character
        elif banner == 'Weap':
            pity = 80 - request.user.profile.weapon
        else:
            pity = 90 - request.user.profile.standard
        return pity * 160 - primogems

    def price(self, request, primo):
        tier6 = primo // 6480
        primo %= 6480
        tier5 = primo // 3280
        primo %= 3280
        tier4 = primo // 1980
        primo %= 1980
        tier3 = primo // 980
        primo %= 980
        tier2 = primo // 300
        primo %= 300
        tier1 = primo // 60
        primo %= 60
        if primo != 0:
            tier1 += 1
        return round((99.99 * tier6) + (49.99 * tier5) + (29.99 * tier4)
            + (14.99 * tier3) + (4.99 * tier2) + (.99 * tier1), 2)

    def Date(self, request, primo):
        days = round(primo / 150 if request.user.profile.blessing else primo / 60, 1)
        Date = date.today()
        Date = Date + datetime.timedelta(days if days % 1 == 0 else days + 1)
        return days, Date.strftime('%B %d, %Y')
