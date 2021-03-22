from django.shortcuts import render,redirect
from .models import blog
from .forms import RegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def blogs(request):
   
    blogs=blog.objects.all()
    return render(request,"index.html",{'blogs':blogs})

def login(request):
    if request.method=="post":
      form=AuthenticationForm(request.POST)
      if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username,password)
        if user is not None:
          login(request,user)
          messages.info(request, f"You are now logged in as:{username}.")
          return redirect("index.html")
        else:
           messages.error(request,"Invalid username or password.")
      else:
          messages.error(request,"Invalid usename or password.")
    form=AuthenticationForm
    return render(request,"login.html",{'login_form':form})

def signup(request):
    if request.method=="post":
      form=RegisterForm(request.POST)
      
    form=RegisterForm
    return render(request,"signup.html",{'register_form':form})
