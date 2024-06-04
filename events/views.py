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
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.success(request,('Hey There is a problem with logging in. Try again..'))
            return redirect('login')
    else:
        return render(request,'authenticate/login.html')
        

