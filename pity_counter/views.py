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
        primogems = self.primogems(request)
        price = self.price(request, primogems)
        days, Date = self.Date(request, primogems)
        context = {
            'primogems': primogems,
            'days': days,
            'date': Date,
            'price': price
            }
        return JsonResponse(context)

    def primogems(self, request):
        banner = request.POST.get('banner', None)
        if banner == 'Char':
            pity = 90 - request.user.profile.character
        elif banner == 'Weap':
            pity = 80 - request.user.profile.weapon
        else:
            pity = 90 - request.user.profile.standard
        return pity * 160 - int(request.POST.get('primogems', None))

    def price(self, request, primo):
        bundles = ((6480, 99.99), (3280, 49.99), (1980, 29.99),
            (980, 14.99), (300, 4.99), (60, 0.99))
        price = 0
        for i in range(6):
            price += (primo // bundles[i][0]) * bundles[i][1]
            primo %= bundles[i][0]
        if primo != 0:
            price += .99
        return round(price, 2)

    def Date(self, request, primogems):
        days = round(primogems / 150 if request.user.profile.blessing else primogems / 60, 1)
        Date = date.today()
        Date = Date + datetime.timedelta(days if days % 1 == 0 else days + 1)
        return days, Date.strftime('%B %d, %Y')
