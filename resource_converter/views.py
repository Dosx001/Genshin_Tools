from django.shortcuts import render, redirect
from django.views.generic import View
import json

class ResourceConverterView(View):
    def get(self, request):
        return render(request, 'resource_converter.html')

    def post(self, request):
        data = json.loads(request.POST.get('data', None))
        print(data)
        return redirect('resource_converter')
