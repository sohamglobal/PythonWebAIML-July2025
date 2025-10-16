from flask import Flask
from flask_restful import Resource, Api
import pymysql

app=Flask(__name__)
api=Api(app)

class EmployeeSearchService(Resource):
    def get(self,loc):
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select * from employees where location='{loc}'")
        data=curs.fetchall()
        lst=[]

        for rec in data:
            dic={}
            dic['name']=rec[1]
            dic['department']=rec[2]
            dic['post']=rec[3]
            dic['location']=rec[4]
            dic['salary']=rec[5]
            lst.append(dic)
        con.close()
        return lst

api.add_resource(EmployeeSearchService,"/emp/search/<loc>")
app.run(debug=True)

        

