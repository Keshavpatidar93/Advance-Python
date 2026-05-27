import pymysql

def read():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from student"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()
    print("Data read successfully...")


def read1():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from student"
    cursor.execute(sql)
    data = cursor.fetchall()
    column = ('id','name','salary')  # touple
    for row in data:
        #print(row)
        print({column[i] : row[i] for i, _ in enumerate(row)})   # enumerate is used to convert it into dictionary
    connection.commit()
    connection.close()
    print("Data read successfully...")


def read2():
    connection = pymysql.connect(host='localhost',user="root",password="root",db="advpython")
    cursor = connection.cursor()
    sql = "select * from student"
    #sql = "select * from student where name like 'r%' "
    #sql = "select * from student where id = 4 "
    #sql = "select * from student where salary = 78000"
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i[0],'\t',i[1],'\t',i[2])
    connection.commit()
    connection.close()
    print("Data read successfully...")


def read3(id,name,salary):
    connection = pymysql.connect(host='localhost', user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from student "

    if id != 0:
        sql = sql + "where id =" + str(id)  # here to connect both the sql query we add both the string and id is an integer that's why we use typeconversion into string
    if name != '':
        sql = sql + "where name like '" + name + "%' "
    if salary != 0:
        sql = sql + "where salary = " + str(salary)

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0],'\t',row[1],'\t',row[2],'\t')
    connection.commit()
    connection.close()
    print("Data read successfully...")


def read4(param={}):
    id = param.get('id',0)
    name = param.get('name','')
    salary = param.get('salary',0)
    connection = pymysql.connect(host='localhost', user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from student where 1=1 "    # 1=1 it is called as sql injection (it adds two sql queres when we use and instead of where )

    if id != 0:
        sql = sql + "and id = " + str(id)
    if name !='':
        sql = sql + "and name like '" + name + "%' "
    if salary != 0:
        sql = sql + "and salary = " + str(salary)
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()
    print("Data read successfully...")


def read5(param={}):
    id = param.get('id',0)
    name = param.get('name','')
    salary = param.get('salary',0)
    pageNo = param.get('pageNo',0)
    pageSize = param.get('pageSize',0)
    connection = pymysql.connect(host='localhost', user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from student where 1=1 "    # 1=1 it is called as sql injection (it adds two sql queres when we use and instead of where )

    if id != 0:
        sql = sql + "and id = " + str(id)
    if name !='':
        sql = sql + "and name like '" + name + "%' "
    if salary != 0:
        sql = sql + "and salary = " + str(salary)

     #paginataion
    if pageSize > 0:
        offset = (pageNo - 1) * pageSize
        sql = sql + "limit " + str(offset) + ","+ str(pageSize)

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()
    print("Data read successfully...")




read()
#read1()
#read2()
#read3(0,'',78000)
#read4({'id':0,'name': "r",'salary':0})
#read5({'id':0,'name': "",'salary':0,'pageNo':3,'pageSize':4})