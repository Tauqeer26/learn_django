from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(requsets):
    now=datetime.datetime.now()
    return render(requsets,"section2/index.html", 
         { "date":now.month==10 and now.day==12}  
           )