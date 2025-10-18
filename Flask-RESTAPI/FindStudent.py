from flask import Flask
from flask_restful import Resource,Api
import pymysql

app=Flask(__name__)
api=Api(app)

class StudentInformation(Resource):
    def get(self,rno):
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select * from students where regno={rno}")
        data=curs.fetchone()
        dic={}
        if data:
            dic['regnumber']=data[0]
            dic['name']=data[1]
            dic['course']=data[2]
        else:
            dic['regnumber']=rno
            dic['name']='Not found'
            dic['course']='Not found'
        
        con.close()
        return dic

api.add_resource(StudentInformation,"/student/search/<rno>")
app.run(debug=True)
