# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html', {
        }, content_type='text/html')
