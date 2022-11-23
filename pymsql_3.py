import pymysql
conn=pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="salami_ty",
    db="customers"
)

increament=10000
key=2
cur=conn.cursor()
sql="""UPDATE bank_customers SET amount = %d WHERE id='%d'
""" %( increament,key)
try:
    cur.execute(sql)
    #result=cur.fetchmany(size=2)
    conn.commit()
except:
    print("error occured")
conn.close()
