import  pymysql

conn =  pymysql.connect(user='root', password='********', host='127.0.0.1', database='customers')#establishing the connection
cursor = conn.cursor()#Creating a cursor object using the cursor() method

cursor.execute("DROP TABLE IF EXISTS bank_customers")#Dropping EMPLOYEE table if already exists.

sql ='''CREATE TABLE bank_customers(
id INT, NOT NULL, AUTO-INCREAMENT,
f_name CHAR(20), NOT NULL,
s_name CHAR(20), NOT NULL,
amt INT, NOT NULL,
mail CHAR(25), NOT NULL,
PRIMARY KEY (id)
)'''
cursor.execute(sql)

conn.close()#Closing the connection
