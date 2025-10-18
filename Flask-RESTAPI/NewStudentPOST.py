from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/student/add',methods=['POST'])
def addnewstudent():
    rno=int(request.form.get('regno'))
    snm=request.form.get('studnm')
    cou=request.form.get('course')
    dic={}
    try:
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"insert into students values({rno},'{snm}','{cou}')")
        con.commit()
        con.close()
        dic['status']='success'
    except:
        dic['status']='failed'
    
    return dic

app.run(debug=True)

