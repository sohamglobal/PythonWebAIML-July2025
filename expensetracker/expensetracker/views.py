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
            request.session['authenticated']=True
            request.session['user']=uid
            return redirect('/dashboard/')
        else:
            request.session['authenticated']=False
            return render(request,"loginfailed.html")


def dashboard(request):
    return render(request,"dashboard.html")

def change(request):
    return render(request,"changepassword.html")

def newexpense(request):
    return render(request,"NewExpense.html")

def addexpense(request):
    msg=''
    if request.method=="POST":
        uid=request.session.get("user")
        dt=request.POST.get("expense_date")
        cat=request.POST.get("category")
        des=request.POST.get("description")
        amt=float(request.POST.get("amount"))
        mode=request.POST.get("paymentmode")
        obj=TrackerServices()
        msg=obj.addnewexpense(uid,dt,cat,des,amt,mode)
    
    return render(request,"ExpenseStatus.html",{'status':msg})

def showreport(request):
    uid=request.session.get('user')
    obj=TrackerServices()
    data=obj.generatereport(uid)
    return render(request,"Report.html",{"expdata":data})

def changepass(request):
    if request.method=="POST":
        uid=request.session.get('user')
        opass=request.POST.get("old_password")
        npass1=request.POST.get("new_password1")
        npass2=request.POST.get("new_password2")
        obj=TrackerServices()
        status=obj.changeuserpassword(uid,opass,npass1,npass2)

    return render(request,"ChangePassStatus.html",{"status":status})    

    