import pymysql
conn=pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="salami_ty",
    db="customers"
)

acc_number=5448
cur=conn.cursor()
sql="""SELECT * FROM bank_customers WHERE account_no ='%d'
""" %(acc_number)
try:
    cur.execute(sql)
    result=cur.fetchall()
    #result=cur.fetchmany(size=2)
    for row in result:
        id=row[0]
        f_name=row[1]
        s_name=row[2]
        acc_no=row[3]
        amt=row[4]
        mail=row[5]
        print(f"id={id},first name={f_name},surname={s_name},account={acc_no},amount={amt},email={mail}")
except:
    print("error occured")
conn.close()
