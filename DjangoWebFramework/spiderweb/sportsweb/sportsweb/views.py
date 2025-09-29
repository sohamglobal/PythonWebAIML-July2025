from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def check(request):
    if request.method=="POST":
        nm=request.POST.get("unm")
        ps=request.POST.get("psw")
        print(f"{nm} | {ps}")
    return render(request,"status.html")