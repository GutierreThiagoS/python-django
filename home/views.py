from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
            "text": 'Estamos na home',
            'title': 'Home'
        }
    return render(
        request, 
        'home/index.html',
        context
    )