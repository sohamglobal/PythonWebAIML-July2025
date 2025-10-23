from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

# http://127.0.0.1:5000/emps
@app.route("/emps", methods=['GET'])
def getemployees():
    con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
    curs=con.cursor()
    curs.execute("select * from employees")
    data=curs.fetchall()
    curs.close()
    con.close()
    return jsonify(data)

@app.route("/emp/add",methods=['POST'])
def addemployee():
    data=request.get_json()
    eno=data.get('empno')
    enm=data.get("empnm")
    dep=data.get("dept")
    po=data.get("post")
    lo=data.get("location")
    sal=data.get("salary")
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

@app.route("/emp/updsal",methods=['PUT'])
def modifysalary():
    #receive data and update
    dic={'status':'success'}
    return dic

@app.route("/emp/del",methods=['DELETE'])
def delemp():
    #receive data and delete
    dic={'status':'success'}
    return dic

app.run(debug=True)
