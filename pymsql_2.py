import pymysql
conn=pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="salami_ty",
    db="customers"
)

data=["Emmanuel","Jideofo",6889,5000,"emmy@gmail.com"]
cur=conn.cursor()
sql="""INSERT INTO bank_customers (fname,sname,account_no,amount,email)
    VALUES ('%s','%s','%d','%d','%s')
""" %(data[0],data[1],data[2],data[3],data[4])
try:
    cur.execute(sql)
    #result=cur.fetchmany(size=2)
    conn.commit()
except:
    print("error occured")
conn.close()
