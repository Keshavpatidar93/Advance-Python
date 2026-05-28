import pymysql

connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
connection.autocommit(True)
cursor = connection.cursor()

sql1 = "insert into marksheet values(16,116,'chetan',67,89,26)"
sql2 = "insert into marksheet values(17,117,'Parth',45,78,56)"
sql3 = "insert into marksheet values(15,116,'chetan',67,89,26)"

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
connection.close()
print("Data added succesfully...")