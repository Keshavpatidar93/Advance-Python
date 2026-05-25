import pymysql
connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
cursor = connection.cursor()
sql="update student set name ='Keshav' where name ='bob'"
cursor.execute(sql)
connection.commit()
connection.close()
