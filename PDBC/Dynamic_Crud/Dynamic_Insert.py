import pymysql

def insert():
    connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
    cursor = connection.cursor()
    sql = "insert into student values(106,'parth',28000)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data inserted succesfully...")


def insert2():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "insert into student values(%s,%s,%s)"
    data = (107,"nilesh",23500)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data inserted 2 succesfully...")

def insert3(id,name,salary):
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "insert into student values(%s,%s,%s)"
    data = (id, name, salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted 3 succesfully...")

def insert4(data={}):
    id = data['id']
    name = data['name']
    salary = data['salary']
    connection = pymysql.connect(host="localhost",port=3306, user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "insert into student values(%s,%s,%s)"
    data = (id, name, salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted 4 succesfully...")


insert()
#insert2()
#insert3(109,'chetan',35800)
#insert4({'id':115   ,'name':'ramesh','salary':89444})