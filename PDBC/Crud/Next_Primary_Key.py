import pymysql
primary_key = 0
connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
cursor = connection.cursor()
sql = "select max(id) from student"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))

for data in result:
    if data[0] is not None:
        primary_key = data[0]

connection.commit()
connection.close()
print("The next primary key is :",primary_key+1)