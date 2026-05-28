import pymysql

def delete1():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "delete from Mobile_Store where Mobile_id = 12"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data deleted successfully....")


def delete2():
    connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
    cursor = connection.cursor()
    sql = "delete from Mobile_Store where RAM = %s "
    data=(18)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data deleted successfully....")


def delete3(Price):
    connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
    cursor = connection.cursor()
    sql = "delete from Mobile_Store where price = %s"
    data = (Price)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data deleted successfully....")


#delete1()
#delete2()
delete3(10000)