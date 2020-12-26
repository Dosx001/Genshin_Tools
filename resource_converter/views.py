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
            drops = self.mastery(int(request.POST.get('adv_rank', None)))
        elif activity == 'Domain of Forgery':
            drops = self.forgery(int(request.POST.get('adv_rank', None)))
        else:
            drops = self.boss(int(request.POST.get('adv_rank', None)))
        if drops == None:
            return JsonResponse(None, safe=False)
        elif data['rarity'] == 2:
            return JsonResponse(self.two_star(drops, data, activity), safe=False)
        elif data['rarity'] == 3:
            return JsonResponse(self.three_star(drops, data, activity), safe=False)
        elif data['rarity'] == 4:
            return JsonResponse(self.four_star(drops, data, activity), safe=False)
        else:
            return JsonResponse(self.five_star(drops, data, activity), safe=False)

    def mastery(self, adv_rank):
        if adv_rank == 27:
            drops = (range(1, 4), range(1), range(1), range(1))
        elif 27 < adv_rank < 36:
            drops = (range(1, 4), range(1, 3), range(1), range(1))
        elif 35 < adv_rank < 45:
            drops = (range(1, 4), range(1, 4), range(1), range(1))
        elif 44 < adv_rank:
            drops = (range(2, 4), range(0, 4), range(0, 3), range(1))
        else:
            return
        return drops

    def forgery(self, adv_rank):
        if 15 < adv_rank < 21:
            drops = (range(4, 7), range(1), range(1), range(1))
        elif 20 < adv_rank < 30:
            drops = (range(2, 4), range(1, 4), range(1), range(1))
        elif 29 < adv_rank < 40:
            drops = (range(0, 4), range(1, 4), range(0, 3), range(1))
        elif 39 < adv_rank:
            drops = (range(2, 4), range(0, 5), range(0, 4), range(0, 2))
        else:
            return
        return drops

    def boss(self, adv_rank):
        if adv_rank < 20: #WL 0
            drops = (range(1, 4), range(1), range(1), range(1))
        elif 19 < adv_rank < 25: #WL 1
            drops = (range(0, 3), range(1, 3), range(1), range(1))
        elif 24 < adv_rank < 30: #WL 2
            drops = (range(1, 3), range(1, 3), range(1), range(1))
        elif 29 < adv_rank < 35: #WL 3
            drops = (range(0, 3), range(1, 3), range(0, 2), range(1))
        elif 34 < adv_rank < 40: #WL 4
            drops = (range(0, 3), range(1, 4), range(0, 2), range(1))
        elif 39 < adv_rank < 45: #WL 5
            drops = (range(0, 4), range(1, 4), range(0, 2), range(0, 2))
        elif 44 < adv_rank < 50: #WL 6
            drops = (range(1, 4), range(1, 3), range(0, 2), range(0, 2))
        elif 49 < adv_rank < 55: #WL 7
            drops = (range(0, 4), range(1, 5), range(0, 2), range(0, 2))
        elif 54 < adv_rank < 61: #WL 8
            drops = (range(1, 3), range(1, 4), range(0, 2), range(0, 2))
        else:
            return
        return drops

    def two_star(self, drops, data, activity):
        records = []
        for i in drops[0]:
            tier2 = data['materials']['star2']
            runs = 0
            while tier2 < data['goal']:
                tier2 += i
                runs += 1
            records.append(self.update_record([i, 0, 0, 0], runs, activity))
        return records

    def three_star(self, drops, data, activity):
        records = []
        for i in drops[1]:
            for j in drops[0]:
                tier2 = data['materials']['star2']
                tier3 = data['materials']['star3']
                runs = 0
                while tier3 < data['goal']:
                    tier2 += j
                    tier3 += i
                    tier3 += tier2 // 3
                    tier2 = tier2 % 3
                    runs += 1
                records.append(self.update_record([j, i, 0, 0], runs, activity))
        return records

    def four_star(self, drops, data, activity):
        records = []
        for i in drops[2]:
            for j in drops[1]:
                for k in drops[0]:
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
                    records.append(self.update_record([k, j, i, 0], runs, activity))
        return records

    def five_star(self, drops, data, activity):
        records = []
        for i in drops[3]:
            for j in drops[2]:
                for k in drops[1]:
                    for l in drops[0]:
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
                        records.append(self.update_record([l, k, j, i], runs, activity))
        return records

    def update_record(self, drops, runs, activity):
        record = {}
        record.update({'drops':drops})
        record.update({'runs':runs})
        resin = runs * 40 if activity == 'Boss' else runs * 20
        record.update({'resin':resin})
        record.update({'days':round(resin / 180, 1)})
        return record
