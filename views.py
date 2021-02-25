from django.shortcuts import render
from django.http import HttpResponse
from .models import player , team
# Create your views here.

def index(request):
    return HttpResponse("<h1>Good!!!! Index function Works!!!!!</h1>")

def contact(request):
    all = player.objects.all()
    html = ''
    for i in all:
        url = str(i.playername) + "-" + str(i.position)
        html += "<li>" + url + "</li>"
    return HttpResponse(html)