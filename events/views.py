from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # process the form data
            pass
    else:
        form = RegisterUserForm()

    return render(request, 'events/home.html', {'form': form})
   
      
    return render(requset,'events/home.html',{
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
        

def logout_user(request):
    logout(request)
    messages.success(request,('Ypu are logged out!! Please log in.'))
    return redirect('login')

def register_user(request):
    if request.method=="POST":
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user= authenticate(username=username,password=password) 
            login(request, user)
            messages.success(request,('Registartion successfull.!!'))
            return redirect('home')
    else:
        form=RegisterUserForm()


    return render(request,'authenticate/register_user.html',{'form':form,})

