from django.shortcuts import render
from django.views.generic import View

from users.models import Profile

class RandomEventView(View):
    def get(self, request):
        context = {
            'profile': Profile() if request.user.is_anonymous else request.user.profile
        }
        return render(request, 'random_event.html', context)
