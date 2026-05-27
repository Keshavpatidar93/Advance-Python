import pymysql

def update():
    connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
    cursor = connection.cursor()
    sql = "update student set name = 'anshu' where name = 'keshav'"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data updated successfully")


def update1():
    connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
    cursor = connection.cursor()
    sql = "update student set name = %s where id = %s"
    data = ('Bharat',1)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data updated successfully")


def update2(name,id):
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "update student set name = %s where id = %s"
    data = (name, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data updated successfully")

def update3(param):
    id = param['id']
    name = param['name']
    salary = param['salary']
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "update student set name = %s,salary = %s where id = %s"
    data = (name,salary,id)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data updated successfully")


#update()
#update1()
#update2('Aaryan',105)
update3({'id':104,'name':'Nehal','salary':51000})