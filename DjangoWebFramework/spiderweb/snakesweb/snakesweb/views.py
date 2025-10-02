from django.shortcuts import render
import pymysql

def home(request):
    return render(request,"index.html",{"devby":"Ethan Hunt","comp":"SohamGlobal"})


def searchstudent(request):
    name=None
    course=None
    if request.method=="POST":
        regno=request.POST.get("regno")
        #select studname,course from students where regno=123
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select studname,course from students where regno={regno}")
        data=curs.fetchone()
        print(data)
        if data:
            name=data[0]
            course=data[1]
        else:
            name='Not found'
            course='Not found'
        con.close()
    return render(request,"studsearchresult.html",{'regno':regno,'name':name,'course':course})

def searchcars(request):
    if request.method=="POST":
        company=request.POST.get("company")
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select * from cars where company='{company}'")
        data=curs.fetchall()
        con.close()
    return render(request,"carsearchresult.html",{"result":data})