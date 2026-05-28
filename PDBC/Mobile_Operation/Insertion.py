import pymysql

def insert1():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "insert into Mobile_Store values(5,'Oppo','Reno 13',8,28000)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data inserted successfully....")


def insert2():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "insert into Mobile_Store values(%s,%s,%s,%s,%s)"
    data = (2,'Samsung','Galaxy',12,45000)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data inserted successfully....")


def insert3(id,brand,model,ram,price):
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "insert into Mobile_Store values(%s,%s,%s,%s,%s)"
    data = (id,brand,model,ram,price)
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    print("Data inserted successfully....")


def insert4(param={}):
    id = param['id']
    brand = param['brand']
    model = param['model']
    ram = param['ram']
    price = param['price']
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "insert into Mobile_Store values(%s,%s,%s,%s,%s)"
    data = (id, brand, model, ram, price)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted successfully....")


insert1()
#insert2()
#insert3(3,'Vivo','v 70',8,40000)
# data = {'id':4,'brand':'Apple','model':'16 pro max','ram':12,'price':13000}
# insert4(data)