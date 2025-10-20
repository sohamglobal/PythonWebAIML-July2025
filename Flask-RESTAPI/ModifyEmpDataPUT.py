from flask import Flask, request
import pymysql

app=Flask(__name__)

@app.route("/emp/modify",methods=['PUT'])
def modifyemp():
    eno=int(request.form.get("empno"))
    loc=request.form.get("location")
    sal=float(request.form.get("salary"))
    dic={}
    try:
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"update employees set location='{loc}',salary={sal} where empno={eno}")
        con.commit()
        dic['status']='success'
        con.close()
    except:
        dic['status']='failed'
    return dic

app.run(debug=True)