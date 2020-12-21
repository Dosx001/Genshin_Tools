from django.shortcuts import render
from django.views.generic import View

class ResourceConverterView(View):
    def get(self, request):
        return render(request, 'resource_converter.html')
