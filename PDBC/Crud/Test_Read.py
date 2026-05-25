import pymysql
connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
cursor = connection.cursor()
sql = "select * from student"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data)
connection.commit()
connection.close()
