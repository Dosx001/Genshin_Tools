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
        else:
            return JsonResponse(self.report(drops, data, activity), safe=False)

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

    def report(self, drops, data, activity):
        records = []
        for i in drops[3]:
            for j in drops[2]:
                for k in drops[1]:
                    for l in drops[0]:
                        star2 = data['materials']['star2']
                        star3 = data['materials']['star3']
                        star4 = data['materials']['star4']
                        if data['rarity'] == 2:
                            runs = self.counter(0, [l], [star2], data['goal'])
                        elif data['rarity'] == 3:
                            runs = self.counter(1, [l, k], [star2, star3], data['goal'])
                        elif data['rarity'] == 4:
                            runs = self.counter(2, [l, k, j], [star2, star3, star4], data['goal'])
                        else:
                            star5 = data['materials']['star5']
                            runs = self.counter(3, [l, k, j, i], [star2, star3, star4, star5], data['goal'])
                        records.append(self.update_record([l, k, j, i], runs, activity))
        return records

    def counter(self, rarity, drops, inventory, goal):
        runs = 0
        while inventory[rarity] < goal:
            inventory[0] += drops[0]
            if rarity > 0:
                inventory[1] += drops[1]
                inventory[1] += inventory[0] // 3
                inventory[0] = inventory[0] % 3
            if rarity > 1:
                inventory[2] += drops[2]
                inventory[2] += inventory[1] // 3
                inventory[1] = inventory[1] % 3
            if rarity > 2:
                inventory[3] += drops[3]
                inventory[3] += inventory[2] // 3
                inventory[2] = inventory[2] % 3
            runs += 1
        return runs

    def update_record(self, drops, runs, activity):
        record = {}
        record.update({'drops':drops})
        record.update({'runs':runs})
        resin = runs * 40 if activity == 'Boss' else runs * 20
        record.update({'resin':resin})
        record.update({'days':round(resin / 180, 1)})
        return record
