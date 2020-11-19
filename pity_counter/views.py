from django.shortcuts import render

def home(request):
    return render(request, 'pity_counter/pity_counter.html')
