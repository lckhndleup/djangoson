from django.shortcuts import render,redirect
from . import forms

from django.contrib.auth import login,authenticate,logout #authenticate db de bilgileri sorgular.varsa objeyi döner yada none döner

from django.contrib.auth.models import User

from django.contrib import messages


# Create your views here.



def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()

            login(request,newUser)
            messages.info(request,"başarıyla kayıt oldunuz..")
            return redirect("index")
        context = {
            "form":form
        }
        return render(request,"register.html",context) 

    else:
        form = forms.RegisterForm()
        context = {
            "form":form
        }
        return render(request,"register.html",context) 

    return render(request, "register.html",context)



def loginUser(request):
    form = forms.LoginForm(request.POST or None)
    context = {

        "form": form
    }

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user = authenticate(username= username,password = password)
        if user is None:
            messages.info(request,"Kullanıcı adı veya Parola hatalı!!")
            """bu durumda kendi bulunduğum sayfaya dönmem gerekiyor."""
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
    



def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış Yaptınız...")
    return redirect("index")
    
