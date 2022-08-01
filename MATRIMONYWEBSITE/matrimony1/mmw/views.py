from django.shortcuts import render,HttpResponseRedirect
from .models import personinfo
from .forms import personform,usersignup
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    if request.method=="POST":
       fm=personform(request.POST,request.FILES)
       if fm.is_valid():
            fm.save()
    else:
       fm=personform()
    pi=personinfo.objects.all()
    return render(request,'index.html',{'fm':fm,'pi':pi})

def info(request):
    pi=personinfo.objects.all()
    return render(request,'register.html',{'pi':pi})

def register(request):
    if request.method=="POST":
       fm=personform(request.POST,request.FILES)
       if fm.is_valid():
            fm.save()
    else:
       fm=personform()
    return render(request,'register.html',{'fm':fm})
    
def detail(request,pk):
  pi=personinfo.objects.get(pk=pk)
  return render(request,'detail.html',{'pi':pi})

def delete_data(request,id):
    pi=personinfo.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method=="POST":
       pi=personinfo.objects.get(pk=id)
       fm=personform(request.POST,request.FILES,instance=pi)
       if fm.is_valid():
        fm.save()
    else:
       pi=personinfo.objects.get(pk=id)
       fm=personform(instance=pi)
    return render(request,'update.html',{'fm':fm})
        
def personinfo1(request):
    pi=personinfo.objects.all()
    return render(request,'person.html',{'pi':pi})
    
def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/person1/')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'fm':fm})

def signup(request):
    if request.method=="POST":
        fm=usersignup(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=usersignup()
    return render(request,'signup.html',{'fm':fm})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def logout1(request):
    logout(request)
    return render(request,'index.html')
    
