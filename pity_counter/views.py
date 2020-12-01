from django.shortcuts import render
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

    def form_valid(self, form):
        if self.request.is_ajax():
            form.instance.by = self.request.user
            print(form.instance.by)
        else:
            print('fasd')

    def post(self, request):
        text = request.POST.get('user')
        print('testing',text)
        print('test')
        request.user.profile.character = 10
        request.user.profile.save()
        context = {
            'profile': request.user.profile,
        }
        return render(request, 'pity_counter/pity_counter.html', context)
        return JsonResponse({'seconds': 123})
