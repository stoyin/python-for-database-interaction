import pymysql
#establishing the connection
conn =  pymysql.connect(user='root', password='******', host='127.0.0.1')#use your own password
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
#Doping database MYDATABASE if already exists.
cursor.execute("DROP database IF EXISTS customers")
#Preparing query to create a database
sql = "CREATE database customers";

#Creating a database
cursor.execute(sql)
#Retrieving the list of databases
print("List of databases: ")
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

#Closing the connection
conn.close()
