from django.shortcuts import render,redirect,HttpResponse

from django.views.generic import View
from django.contrib.auth.models import User
from anwar.models import *
from django.contrib.auth import authenticate,login


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'homepage.html')
class Register(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
            data = request.POST
            email = data["email"]
            fullname = data["fullname"]
            passw = data["pass"]
            fn=data["fn"]
            ln=data["ln"]
            r1 = User.objects.create_user(username=fullname, password=passw, email=email,
                                            first_name=fn,last_name=ln)
            r1.save()
            return redirect('home')
class Log(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        data = request.POST
        us = data["username"]
        pas = data["pass"]
        user = authenticate(request, username=us, password=pas)
        if user is not None:
            login(request, user)
            return redirect('/mainhome/')
        else:

            return HttpResponse("invalid user")
class Mainhome(View):
    def get(self,request):
        return render(request,'mainhome.html')
