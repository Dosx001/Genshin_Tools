from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
import json

class ResourceConverterView(View):
    def get(self, request):
        return render(request, 'resource_converter.html')

    def post(self, request):
        data = json.loads(request.POST.get('data', None))
        activity = request.POST.get('activity', None)
        if activity == 'Domain of Mastery':
            rates = self.mastery(int(request.POST.get('adv_rank', None)))
        elif activity == 'Domain of Forgery':
            rates = self.forgery(int(request.POST.get('adv_rank', None)))
        else:
            rates = self.boss(int(request.POST.get('adv_rank', None)))
        if rates == None:
            return JsonResponse(None, safe=False)
        elif data['rarity'] == 2:
            return JsonResponse(self.two_star(rates, data, activity), safe=False)
        elif data['rarity'] == 3:
            return JsonResponse(self.three_star(rates, data, activity), safe=False)
        elif data['rarity'] == 4:
            return JsonResponse(self.four_star(rates, data, activity), safe=False)
        else:
            return JsonResponse(self.five_star(rates, data, activity), safe=False)

    def mastery(self, adv_rank):
        if adv_rank == 27:
            rates = (range(1, 4), )
        elif 27 < adv_rank < 36:
            rates = (range(1, 4), range(1, 3))
        elif 35 < adv_rank < 45:
            rates = (range(1, 4), range(1, 4))
        elif 44 < adv_rank:
            rates = (range(2, 4), range(0, 4), range(0, 3))
        else:
            return
        return rates

    def forgery(self, adv_rank):
        if 15 < adv_rank < 21:
            rates = (range(4, 7), )
        elif 20 < adv_rank < 30:
            rates = (range(2, 4), range(1, 4))
        elif 29 < adv_rank < 40:
            rates = (range(0, 4), range(1, 4), range(0, 3))
        elif 39 < adv_rank:
            rates = (range(2, 4), range(0, 5), range(0, 4), range(0, 2))
        else:
            return
        return rates

    def boss(self, adv_rank):
        if adv_rank < 20:
            rates = (range(1, 3), )
        elif 19 < adv_rank < 25:
            rates = (range(1, 3), range(1, 2))
        elif 24 < adv_rank < 30:
            rates = (range(1, 3), range(1, 3))
        elif 29 < adv_rank < 35:
            rates = (range(2, 3), range(0, 3), range(0, 2))
        elif 34 < adv_rank < 40:
            rates = (range(2, 3), range(0, 3), range(0, 2))
        elif 39 < adv_rank < 45:
            rates = (range(2, 3), range(0, 3), range(0, 2))
        elif 44 < adv_rank < 50:
            rates = (range(2, 3), range(0, 3), range(0, 2))
        elif 49 < adv_rank < 55:
            rates = (range(2, 3), range(0, 3), range(0, 2))
        elif 54 < adv_rank < 61:
            rates = (range(2, 3), range(0, 3), range(0, 2))
        else:
            return
        return rates

    def two_star(self, rates, data, activity):
        records = []
        for i in rates[0]:
            tier2 = data['materials']['star2']
            runs = 0
            while tier2 < data['goal']:
                tier2 += i
                runs += 1
            records.append(self.update_record(i, runs, activity))
        return records

    def three_star(self, rates, data, activity):
        records = []
        for i in rates[1]:
            for j in rates[0]:
                tier2 = data['materials']['star2']
                tier3 = data['materials']['star3']
                runs = 0
                while tier3 < data['goal']:
                    tier2 += j
                    tier3 += i
                    tier3 += tier2 // 3
                    tier2 = tier2 % 3
                    runs += 1
                records.append(self.update_record(i, runs, activity))
        return records

    def four_star(self, rates, data, activity):
        records = []
        for i in rates[2]:
            for j in rates[1]:
                for k in rates[0]:
                    tier2 = data['materials']['star2']
                    tier3 = data['materials']['star3']
                    tier4 = data['materials']['star4']
                    runs = 0
                    while tier4 < data['goal']:
                        tier2 += k
                        tier3 += j
                        tier3 += tier2 // 3
                        tier2 = tier2 % 3
                        tier4 += i
                        tier4 += tier3 // 3
                        tier3 = tier3 % 3
                        runs += 1
                    records.append(self.update_record(i, runs, activity))
        return records

    def five_star(self, rates, data, activity):
        records = []
        for i in rates[3]:
            for j in rates[2]:
                for k in rates[1]:
                    for l in rates[0]:
                        tier2 = data['materials']['star2']
                        tier3 = data['materials']['star3']
                        tier4 = data['materials']['star4']
                        tier5 = data['materials']['star5']
                        runs = 0
                        while tier5 < data['goal']:
                            tier2 += l
                            tier3 += k
                            tier3 += tier2 // 3
                            tier2 = tier2 % 3
                            tier4 += j
                            tier4 += tier3 // 3
                            tier3 = tier3 % 3
                            tier5 += i
                            tier5 += tier4 // 3
                            runs += 1
                        records.append(self.update_record(i, runs, activity))
        return records

    def update_record(self, rate, runs, activity):
        record = {}
        record.update({'rate':rate})
        record.update({'runs':runs})
        resin = runs * 40 if activity == 'Boss' else runs * 20
        record.update({'resin':resin})
        record.update({'days':round(resin / 180, 1)})
        return record
