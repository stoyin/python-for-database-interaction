import pymysql #establishing the connection
conn =  pymysql.connect(user='root', password='******', host='127.0.0.1')#Creating a cursor object using the cursor() method

cursor = conn.cursor()#Doping database MYDATABASE if already exists.

cursor.execute("DROP database IF EXISTS customers")#Preparing query to create a database
sql = "CREATE database customers";
cursor.execute(sql)#Creating a database

print("List of databases: ")
cursor.execute("SHOW DATABASES")#Retrieving the list of databases
print(cursor.fetchall())

conn.close()#Closing the connection
