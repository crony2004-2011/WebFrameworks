from django.shortcuts import render
from django.http import HttpResponse
from appdj.models import player , team , grounds
from django.template import loader
from appdj.form import contactform
# Create your views here.
from appdj.form import *

def index(request):
    return HttpResponse("<h1>Index function works</h1>")
def intro(requet):
    return HttpResponse("<h1>Welcome to Intro Page and the intro function works</h1>")

def contact(request):
    all = player.objects.all()
    html = ''
    for i in all:
        url = str(i.playername) + "-" + str(i.position)
        html += "<li>" + url + "</li>"
    return HttpResponse(html)

def forms(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name,email)

    form = contactform()
    return render(request, 'html/forms.html', {'form' : form})

def teams(request):
    alll = team.objects.all()
    html = ''
    for i in alll:
        url = str(i.name) + "-" + str(i.location)
        html += "<li>" + url + "</li>"
    return HttpResponse(html)

def templates(request):
    allll = team.objects.all()
    alllll = player.objects.all()
    #template = loader.get_template('html/temp.html')
    #this step is wierd but INFORMATION CAN BE PASSED TO THE HTML PAGE THROUGH DICTIONARY ONLY.
    context = {
        'alllll' : alllll,
        'allll' : allll ,
    }
    #we can either use render or template method, render function ofcourse had less syntax
    return render(request , 'html/temp.html' , context)
    #return HttpResponse(template.render(context, request))

def arsenal(request):
    allll = team.objects.all()
    return render(request, 'html/arsenal.html')

def chelsea(request):
    allll = team.objects.all()
    return render(request, 'html/chelsea.html')

def modelform(request):
    if request.method == 'POST':
        form = gr(request.POST)
        if form.is_valid():
            print('valid')

    form = gr()
    return render(request, 'html/modelform.html', {'form' : form})


