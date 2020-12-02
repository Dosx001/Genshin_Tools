from django.shortcuts import render, redirect
from django.views.generic import View

from users.models import Profile

class RandomEventView(View):
    def get(self, request):
        context = {
            'profile': Profile() if request.user.is_anonymous else request.user.profile
        }
        return render(request, 'random_event.html', context)

    def post(self, request):
        if not request.user.is_anonymous:
            request.user.profile.event -= 1
            request.user.profile.save()
        return redirect('random_event')
