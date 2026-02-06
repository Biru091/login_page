from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

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


def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username1")
        password=request.POST.get("password1")
        if not User.objects.filter(username=username).exists():
            messages.info(request,'Username does not exists!')

            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'User password is wrong!')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/main/')
    return render(request,'core/login.html')

def main(request):
    return render (request,'core/main.html')