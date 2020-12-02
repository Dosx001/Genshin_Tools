from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils import timezone

from users.models import Profile

class RandomEventView(View):
    def get(self, request):
        if (not request.user.is_anonymous and
            request.user.profile.date.date() != timezone.now().date()):
            request.user.profile.date = timezone.now()
            request.user.profile.event = 10
            request.user.profile.save()
        context = {
            'profile': Profile() if request.user.is_anonymous else request.user.profile
        }
        return render(request, 'random_event.html', context)

    def post(self, request):
        if not request.user.is_anonymous:
            request.user.profile.event -= 1
            request.user.profile.save()
        return redirect('random_event')
