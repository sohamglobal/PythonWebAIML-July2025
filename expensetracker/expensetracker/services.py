import pymysql

class TrackerServices:
    def addnewuser(self,uid,ps,nm,mob,age,gen,occ,ct):
        try:
            con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
            curs=con.cursor()
            curs.execute(f"insert into users values('{uid}','{ps}','{nm}','{mob}',{age},'{gen}','{occ}','{ct}')")
            con.commit()
            msg='success'
            con.close()
        except:
            msg='failed'
        
        return msg
    
    def checkuser(self,uid,ps):
        try:
            con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
            curs=con.cursor()
            curs.execute(f"select * from users where userid='{uid}' and password='{ps}'")
            data=curs.fetchone()
            if data:
                msg='success'
            else:
                msg='failed'
            con.close()
        except:
            msg='failed'
        return msg
    
    def addnewexpense(self,uid,dt,cat,des,amt,mode):
        try:
            con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
            curs=con.cursor()
            curs.execute(f"insert into expenses(userid,expense_date,category,description,amount,paymentmode) values('{uid}','{dt}','{cat}','{des}',{amt},'{mode}')")
            con.commit()
            msg='Expense entry recorded successfully'
            con.close()
        except:
            msg='Expense entry failed'

        return msg
    
    def generatereport(self,uid):
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select * from expenses where userid='{uid}'")
        data=curs.fetchall()
        con.close()
        return data
    
    def changeuserpassword(self,uid,opass,npass1,npass2):
        if npass1==npass2:
            con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
            curs=con.cursor()
            cnt=curs.execute(f"update users set password='{npass1}' where userid='{uid}' and password='{opass}'")
            con.commit()
            if cnt>0:
                status="Password changed successfully"
            else:
                status="Current password incorrect"
            con.close()
        else:
            status="New passwords mismatched"
        return status
    
    def searchexpondate(self,uid,sdt):
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"select * from expenses where userid='{uid}' and expense_date='{sdt}'")
        data=curs.fetchall()
        con.close()
        return data
    
    def deleteexpense(self,uid,eid):
        con=pymysql.connect(host='mysql-pyprojects-python-apps.b.aivencloud.com',port=18733,user='praffull',password='AVNS_rAHnLeXr31XIltE9DAh',database='sharayudb')
        curs=con.cursor()
        cnt=curs.execute(f"delete from expenses where userid='{uid}' and expenseid={eid}")
        con.commit()
        if cnt==1:
            msg="Expense entry deleted"
        else:
            msg="Not Found for the user"
        con.close()
        return msg
