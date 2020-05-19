from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import requests as rq
from bs4 import BeautifulSoup

# Create your views here.

def index(request):

  URL = 'https://www.cyclocane.com/amphan-storm-tracker/'
  page_content = rq.get(URL).content
  soup = BeautifulSoup(page_content,'html.parser')
  current_speed = float(soup(class_='low')[1].text[:-3])*1.60934
  return render(request,'index.html',{'current_speed':round(current_speed,2)})

def forecast_track(request):
  return render(request,'forecast_track.html')

def amisafe(request):
  return render(request,'amisafe.html')