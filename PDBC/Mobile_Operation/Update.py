import pymysql

def update1():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "update Mobile_Store set Model_Name = '10 pro max' where Brand_Name = 'Redmi'"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data updated successfully....")


def update2():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "update Mobile_Store set Model_Name = %s where Mobile_id = %s "
    data = ('S 24',2)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data updated successfully....")


def update3(Model_Name,Price):
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "update Mobile_Store set Price = %s where Model_Name = %s "
    data = (Price,Model_Name)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data updated successfully....")


def update4(param={}):
    Brand =param['Brand_Name']
    price = param['Price']
    connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
    cursor = connection.cursor()
    sql = "update Mobile_Store set price = %s where Brand_Name = %s"
    data = (price,Brand)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data updated successfully....")


#update1()
#update2()
#update3("16 Pro Max",130000)
data = {'Price':35000,'Brand_Name':'Oppo'}
update4(data)