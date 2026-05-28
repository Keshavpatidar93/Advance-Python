import pymysql

def delete():
    connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
    cursor = connection.cursor()
    sql = "delete from student where id=114"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data deleted successfully....")


def delete1():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "delete from student where id = %s "
    data=(115)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data deleted successfully....")


def delete2(name):
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "delete from student where name = %s "
    data=(name)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data deleted successfully....")


# delete()
# delete1()
delete2("jayesh")