from flask import Flask, request
import pymysql
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/bank/transfer",methods=['PUT'])
def transfermoney():
    fno=int(request.form.get("fromacc"))
    tno=int(request.form.get("toacc"))
    amt=float(request.form.get("amount"))
    dic={}
    try:
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"update accounts set balance=balance-{amt} where accno={fno}")
        curs.execute(f"update accounts set balance=balance+{amt} where accno={tno}")
        con.commit()
        dic['message']='transfer successful'
        con.close()
    except:
        dic['message']='transaction failed'
    
    return dic

app.run(debug=True)