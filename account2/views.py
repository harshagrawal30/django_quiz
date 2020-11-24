from django.shortcuts import render,redirect
from .models import user_info
from django.contrib import messages
from django.contrib.auth.models import User,auth
from random import *
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        classnum=int(request.POST['classnum'])
        
        user=user_info()
        user.username=first_name.capitalize()+' '+last_name.capitalize()
        user.username1=first_name.capitalize()+'_'+last_name.capitalize()
        usrnme=user.username1+str(randint(1,10000))
        usrnme2=usrnme.upper()
        user.password1=password1
        user.password2=password2
        user.classnum=classnum
        user.username1=usrnme2
        if password1!='':
            if(password1==password2):
                
                Users=User.objects.create_user(first_name=first_name,last_name=last_name,password=password1,username=usrnme2)
                
                Users.save();
                
                user.save();
            else:
                messages.info(request,'password does not  matched')
                return redirect('register')
        else:
            messages.info(request,'Please enter password')
            return redirect('register')
        message='Your username(Remember it) generated is '+usrnme2
        return render(request,'login.html',{'username':message})
    else:
        return render(request,'register.html')



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid entries')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')