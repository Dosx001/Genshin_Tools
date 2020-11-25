from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import JsonResponse

class PityCounterView(View):
    def get(self, request):
        context = {
            'profile': request.user.profile,
        }
        return render(request, 'pity_counter/pity_counter.html', context)

    def post(self, request):
        text = request.POST.get('buttum_text')
        print(text)
        print('test')
        return JsonResponse({'seconds': 123})

def Weapon10(request):
    char = request.GET.get('buttum_num', None)
    if char <= 80:
        request.user.profile.character = 0
    else:
        request.user.profile.character += 10
    print(request.user.profile.character)
#    return home(request)
