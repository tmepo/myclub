from django.shortcuts import render
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
# Create your views here.
def home(requset):
    name='nothing'
   
      
    return render(requset,'events/home.html',{
        'name':name,
    }
    )
def search_anything(request):
    if request.method=="POST":
        searched=request.POST['searched']
        return render(request,'events/searched.html',{'searched':searched})
    else:
        return render(request,'events/searched.html',{})
        

