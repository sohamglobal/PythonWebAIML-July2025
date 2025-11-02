from django.shortcuts import render, redirect
from pymongo import MongoClient

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
            client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.vzrlbsf.mongodb.net/?appName=sharayucluster")
            db=client["jobprojectdb"]
            coll=db["users"]
            coll.insert_one(dic)
            msg="success"
        except:
            msg="failed"
    
    return render(request,"registered.html",{"status":msg})

def login(request):
    return render(request,"jobseeker.html")