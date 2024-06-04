from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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
    
def login_user(request):
    return render(request,'authenticate/login.html')
        

