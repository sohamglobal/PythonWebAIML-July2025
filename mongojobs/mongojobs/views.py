from django.shortcuts import render, redirect
from django.conf import settings

def home(request):
    return render(request,"index.html")

def register(request):
    return render(request,"userregistration.html")


def adduser(request):
    if request.method=="POST":
        uid=request.POST.get("userid")
        psw=request.POST.get("password")
        typ=request.POST.get("usertype")
        print(f"{uid} | {psw} | {typ}")
        dic={}
        dic["userid"]=uid
        dic["password"]=psw
        dic["usertype"]=typ
        print(dic)
        try:
            coll=settings.DB["users"]
            coll.insert_one(dic)
            msg="success"
        except Exception as e:
            print(e)
            msg="failed"
    
    return render(request,"registered.html",{"status":msg})

def login(request):
    if request.method=="POST":
        uid=request.POST.get("userid")
        ps=request.POST.get("password")
        coll=settings.DB["users"]
        user=coll.find_one({"userid":uid,"password":ps})
        print(user)

        if user:
            request.session['authenticated']=True
            request.session['user']=uid
            if user["usertype"]=="Seeker":
                return redirect('/seeker/')
            else:
                return redirect("/recruiter/")
        else:
            request.session['authenticated']=False
            return render(request,"loginfailed.html")
   
    


def seeker(request):
    return render(request,"jobseeker.html")

def recruiter(request):
    return render(request,"recruiter.html")

def newprofile(request):
    return render(request,"newprofile.html")

def addprofile(request):
    if request.method=="POST":
        nm=request.POST.get("name")
        gn=request.POST.get("gender")
        ag=int(request.POST.get("age"))
        ct=request.POST.get("city")
        mo=request.POST.get("mobile")
        em=request.POST.get("emailid")
        ql=request.POST.get("qualification")
        ex=int(request.POST.get("experience"))
        ln=request.POST.getlist("languages")
        db=request.POST.getlist("databases")
        fr=request.POST.getlist("frameworks")
        cl=request.POST.getlist("cloud")
        ai=request.POST.getlist("ai_models")
        dic={}
        dic["userid"]=request.session.get('user')
        dic["name"]=nm
        dic["gender"]=gn
        dic["age"]=ag
        dic["city"]=ct
        dic["mobile"]=mo
        dic["emailid"]=em
        dic["qualification"]=ql
        dic["experience"]=ex
        dic["languages"]=ln
        dic["databases"]=db
        dic["frameworks"]=fr
        dic["cloud"]=cl
        dic["aimodels"]=ai
        coll=settings.DB["profiles"]
        coll.insert_one(dic)
    return render(request,"profileadded.html")