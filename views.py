from django.shortcuts import render, get_object_or_404
import requests
from bs4 import BeautifulSoup
from .models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'home.html',{'context':'Welcome'})

def form(request):
    return render(request, 'form.html')

def transfers(request):
    url = "https://www.sportsmole.co.uk/football/man-utd/transfer-talk/feature/premier-league-transfer-ins-and-outs-summer-2020_404715.html"
    x = requests.get(url)
    soup = BeautifulSoup(x.content, 'html.parser')
    soup_body = soup.find('div', id='article_body')
    soup1 = soup_body.find_all('p')[4].getText()
    soup2 = soup_body.find_all('p')[5].getText()
    soup3 = soup_body.find_all('p')[7].getText()
    soup4 = soup_body.find_all('p')[8].getText()
    soup5 = soup_body.find_all('p')[9].getText()
    soup6 = soup_body.find_all('p')[11].getText()
    context = {'soup1': soup1, 'soup2': soup2, 'soup3': soup3, 'soup4': soup4, 'soup5': soup5,'soup6':soup6}
    return render(request, 'success.html', context)

def form_to_model(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        city = request.POST['city']
        address = request.POST['address']
        email = request.POST['email']
        query = request.POST['query']
        form_query = formquery(name=name, phone=phone, city=city, address=address, email=email, Query=query)
        form_query.save()
        return render(request, 'form.html')

def queries(request):
    x = formquery.objects.all()
    context = {'x': x}
    return render(request, 'customer_query.html', context)

def signup(request):
    return render(request,'signup.html')

