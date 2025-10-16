from flask import Flask
from flask_restful import Resource, Api
import pymysql

app=Flask(__name__)
api=Api(app)

class AccountInformationService(Resource):
    def get(self,ano):
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select * from accounts where accno={ano}")
        data=curs.fetchone()
        print(data)
        dic={}
        if data:
            dic['accountnumber']=data[0]
            dic['name']=data[1]
            dic['type']=data[2]
            dic['balance']=data[3]
        else:
            dic['accountnumber']=ano
            dic['name']='Not found'
            dic['type']='Not found'
            dic['balance']=0
        
        con.close()
        return dic

api.add_resource(AccountInformationService,"/account/search/<ano>")
app.run(debug=True)

# http://127.0.0.1:5000/account/search/1044
