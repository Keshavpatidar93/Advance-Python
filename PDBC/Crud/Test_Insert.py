import pymysql

connection = pymysql.connect(host="localhost", user='root', password='root', db='advpython')
curser = connection.cursor()
sql = "insert into student values(104,'Uday')"
curser.execute(sql)
connection.commit()
connection.close()
print("Data Inserted Successfully....")
