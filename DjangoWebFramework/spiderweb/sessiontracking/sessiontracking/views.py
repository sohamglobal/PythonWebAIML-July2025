from django.shortcuts import render

def home_view(request):
    return render(request,"index.html")


def check(request):
    error=''
    if request.method=="POST":
        userid=request.POST.get("userid")
        password=request.POST.get("password")

        if password=='spider':
            request.session['authenticated']=True
            request.session['user']=userid
            return render(request,"customer.html")
        else:
            error='Authentication failed'
    
    return render(request,"index.html",{'error':error})

def history(request):
    uid=request.session.get('user')
    return render(request,"ShoppingHistory.html",{'userid':uid})