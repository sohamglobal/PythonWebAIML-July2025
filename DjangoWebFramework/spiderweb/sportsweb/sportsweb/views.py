from django.shortcuts import render
import pymysql

def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def check(request):
    if request.method=="POST":
        nm=request.POST.get("unm")
        ps=request.POST.get("psw")
        print(f"{nm} | {ps}")
        stat=None
        if ps=='chelsea786':
            stat='success'
        else:
            stat='failed'

    return render(request,"status.html",{"usernm":nm,"userstatus":stat})

def newstudent(request):
    return render(request,"newstudententry.html")

def addstudent(request):
    if request.method=="POST":
        regno=request.POST.get("regno")
        studname=request.POST.get("studname")
        course=request.POST.get("course")
        print(f"{regno} | {studname} | {course}")

        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"insert into students values({regno},'{studname}','{course}')")
        con.commit()
        print('new student added successfully')
        con.close()
   
    return render(request,"AddStudent.html")