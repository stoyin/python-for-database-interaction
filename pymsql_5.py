import pymysql

class DBHelper:

    def __init__(self):
        self.host="127.0.0.1"
        self.user='root'
        self.password="**************"
        self.db="***********"

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
                details=(id,f_name,s_name,acc_no,amt,mail)
                return details
                #print(f"id={id},first name={f_name},surname={s_name},account={acc_no},amount={amt},email={mail}")

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

    def transfer(self, key1, key2, t_fund):
        self.decrease(key1, t_fund)
        self.increase(key2, t_fund)



    def verify(self, acc):
        self.__connect__()
        sql="""SELECT fname, sname FROM bank_customers WHERE account_no='%d' """ %(acc)
        try:
            self.cur.execute(sql)
            res=self.cur.fetchall()
            if len(res) != 0:
                for x in res:
                    f_name = x["fname"]
                    s_name = x["sname"]
                print(f"Account holder is {f_name} {s_name}")
            else:
                print("sorry, could not verify account holder!")
        except:
            print("error occured")
        self.__disconnect__()


'''
marko=DBHelper()
#marko.select(5449)
data=["Tarri","Zakana",4244,5000,"zakana@gmail.com"]
data_1=[("Eukera","Eze",4385,5000,"eukera@gmail.com"),
        ("Moses","Ayuba",4789,5000,"molex@gmail.com"),
        ("Joy","Clement",5679,5000,"oclement@gmail.com")]
#marko.insert(data)
#marko.insert_plenty(data_1)
marko.increase(10,5000)
mat=DBHelper()
mat.transfer(6,5,1000)
mat.verify(4789)
mat=DBHelper()
mat.verify(5449)

mat=DBHelper()
mat.verify(4000)

'''
