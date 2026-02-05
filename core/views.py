from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    return render(request,"core/Home.html")
def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')
        if pass1 == pass2:
            user=User.objects.create (
                username=username,
                email=email,

            )
            user.set_password(pass1)
            user.save()
            messages.info(request,"Account created successfully. ")
            return redirect('/login/')
        else:
            messages.info(request,"Pleas enter same password.")
            return redirect('/register/')







    return render(request,"core/register.html")
def login(request):
    return render(request,'core/login.html')
