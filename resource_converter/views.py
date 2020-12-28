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
            drops = self.mastery(request.POST.get('usr_info', None))
        elif activity == 'Domain of Forgery':
            drops = self.forgery(request.POST.get('usr_info', None))
        else:
            drops = self.boss(int(request.POST.get('usr_info', None)))
        if drops == None:
            return JsonResponse(None, safe=False)
        else:
            return JsonResponse(self.report(drops, data, activity), safe=False)

    def mastery(self, usr_info):
        if usr_info == '27':
            drops = (range(1, 4), range(1), range(1), range(1))
        elif usr_info == '28 to 35':
            drops = (range(1, 4), range(1, 3), range(1), range(1))
        elif usr_info == '36 to 44':
            drops = (range(1, 4), range(1, 4), range(1), range(1))
        else:
            drops = (range(2, 4), range(0, 4), range(0, 3), range(1))
        return drops

    def forgery(self, usr_info):
        if usr_info == '16 to 20':
            drops = (range(4, 7), range(1), range(1), range(1))
        elif usr_info == '21 to 29':
            drops = (range(2, 4), range(1, 4), range(1), range(1))
        elif usr_info == '30 to 39':
            drops = (range(0, 4), range(1, 4), range(0, 3), range(1))
        else:
            drops = (range(2, 4), range(0, 5), range(0, 4), range(0, 2))
        return drops

    def boss(self, usr_info):
        if usr_info == 0:
            drops = (range(1, 4), range(1), range(1), range(1))
        elif usr_info == 1:
            drops = (range(0, 3), range(1, 3), range(1), range(1))
        elif usr_info == 2:
            drops = (range(1, 3), range(1, 3), range(1), range(1))
        elif usr_info == 3:
            drops = (range(0, 3), range(1, 3), range(0, 2), range(1))
        elif usr_info == 4:
            drops = (range(0, 3), range(1, 4), range(0, 2), range(1))
        elif usr_info == 5:
            drops = (range(0, 4), range(1, 4), range(0, 2), range(0, 2))
        elif usr_info == 6:
            drops = (range(1, 4), range(1, 3), range(0, 2), range(0, 2))
        elif usr_info == 7:
            drops = (range(0, 4), range(1, 5), range(0, 2), range(0, 2))
        else:
            drops = (range(1, 3), range(1, 4), range(0, 2), range(0, 2))
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
                        records.append(self.update_record(
                            [l, k, j] if activity == 'Domain of Mastery' else [l, k, j, i],
                            runs, activity
                            )
                        )
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
