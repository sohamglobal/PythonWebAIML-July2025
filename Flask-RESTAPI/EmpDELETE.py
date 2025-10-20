from flask import Flask, request
import pymysql

app=Flask(__name__)

@app.route("/emp/delete",methods=['DELETE'])
def delemployee():
    eno=int(request.form.get("empno"))
    dic={}
    try:
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        cnt=curs.execute(f"delete from employees where empno={eno}")
        con.commit()
        if cnt==1:
            dic['status']='success'
        else:
            dic['status']='not found'
        con.close()
    except:
        dic['status']='failed'
    return dic

app.run(debug=True)
        