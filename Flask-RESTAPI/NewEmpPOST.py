from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/emp/add',methods=['POST'])
def addnewemp():
    eno=int(request.form.get('empno'))
    enm=request.form.get('empnm')
    dep=request.form.get('dept')
    po=request.form.get('post')
    lo=request.form.get('location')
    sal=float(request.form.get('salary'))
    dic={}
    try:
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"insert into employees values({eno},'{enm}','{dep}','{po}','{lo}',{sal})")
        con.commit()
        con.close()
        dic['status']='success'
    except:
        dic['status']='failed'
    
    return dic


app.run(debug=True)
