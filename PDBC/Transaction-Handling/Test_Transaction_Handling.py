import pymysql
connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")

try:
    connection.autocommit(False)
    cursor = connection.cursor()
    sql1 = "insert into marksheet values(18,118,'Rahul',45,67,89)"
    sql2 = "insert into marksheet values(19,119,'Golu',56,37,99)"
    sql3 = "insert into marksheet values(16,116,'Raju',45,67,89)"

    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    connection.commit()
    print("Data inserted successfully....")

except Exception as e:
    connection.rollback()
    print("Transection rolled back due to error  :",e)