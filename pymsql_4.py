import pymysql

class DBHelper:
    def __init__(self):
        self.host="127.0.0.1"
        self.user='root'
        self.password="salami_ty"
        self.db="customers"

    def __connect__(self):
        self.con=pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            cursorclass=pymysql.cursors.DictCursor

        )
        self.cur=self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def select(self,acc):
        self.__connect__()
        sql='''SELECT * FROM  bank_customers WHERE account_no= '%d'  ''' %(acc)
        try:
            self.cur.execute(sql)
            res=self.cur.fetchall()
            for row in res:
                #print(row)
                id = row['id']
                f_name = row['fname']
                s_name = row['sname']
                acc_no = row['account_no']
                amt = row['amount']
                mail = row['email']
                print(f"id={id},first name={f_name},surname={s_name},account={acc_no},amount={amt},email={mail}")

        except:
            print("error")
        self.__disconnect__()

	

    
    def insert(self,data):
        self.__connect__()
        sql='''INSERT INTO bank_customers (fname,sname,account_no,amount,email)VALUES ('%s','%s','%d','%d','%s')''' %(data[0],data[1],data[2],data[3],data[4])
        try:
            self.cur.execute(sql)
            # result=cur.fetchmany(size=2)
            self.con.commit()
        except:
            print("error occured")
        self.__disconnect__()	



     def insert_plenty(self,data):
        self.__connect__()
        sql='''INSERT INTO bank_customers (fname,sname,account_no,amount,email)VALUES (%s,%s,%s,%s,%s)'''
        try:
            self.cur.executemany(sql,data)
            self.con.commit()
        except:
            print("error occured")
        self.__disconnect__()


        def increase(self,key,increament):
        self.__connect__()
        sql = """UPDATE bank_customers SET amount = amount + %d WHERE id='%d'
        """ % (increament, key)
        try:
            self.cur.execute(sql)
            self.con.commit()
        except:
            print("error occured")
        self.__disconnect__()
	

     def decrease(self,key,decreament):
        self.__connect__()
        sql = """UPDATE bank_customers SET amount = amount - %d WHERE id='%d'
        """ % (decreament, key)
        try:
            self.cur.execute(sql)
            self.con.commit()
        except:
            print("error occured")
        self.__disconnect__()
