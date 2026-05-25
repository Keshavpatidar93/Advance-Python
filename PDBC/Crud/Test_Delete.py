import pymysql
connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
cursor = connection.cursor()
sql = "delete from student where id=101"
cursor.execute(sql)
connection.commit()
connection.close()