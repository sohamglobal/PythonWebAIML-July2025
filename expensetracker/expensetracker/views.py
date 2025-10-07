from django.shortcuts import render,redirect
from .services import TrackerServices

def homepage(request):
    return render(request,"index.html")

def registerform(request):
    return render(request,"UserRegistration.html")

def adduser(request):

    if request.method=="POST":
        uid=request.POST.get("userid")
        ps=request.POST.get("password")
        nm=request.POST.get("username")
        mob=request.POST.get("mobile")
        age=int(request.POST.get("age"))
        gen=request.POST.get("gender")
        occ=request.POST.get("occupation")
        ct=request.POST.get("city")
        obj=TrackerServices()
        msg=obj.addnewuser(uid,ps,nm,mob,age,gen,occ,ct)
    
    return render(request,"RegisterStatus.html",{'status':msg,'name':nm})

def login(request):
    if request.method=="POST":
        uid=request.POST.get("userid")
        ps=request.POST.get("password")
        obj=TrackerServices()
        status=obj.checkuser(uid,ps)

        if status=='success':
            return redirect('/dashboard/')
        else:
            return render(request,"loginfailed.html")


def dashboard(request):
    return render(request,"dashboard.html")

def change(request):
    return render(request,"changepassword.html")

    