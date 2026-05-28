import pymysql

def read1():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from Mobile_Store"
    #sql = "select * from Mobile_Store where Brand_Name like 'a%' "
    #sql = "select * from Mobile_Store where Mobile_id = 4 "
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()
    print("Execution completed Successfully")


def read2():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from Mobile_Store"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t')
    connection.commit()
    connection.close()
    print("Execution completed Successfully")


def read3():
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from Mobile_Store"
    cursor.execute(sql)
    data = cursor.fetchall()
    column = ("Mobile_id","Brand_Name","Model_Name","RAM","Price")   # touple
    for row in data:
        print({column[i]:row[i] for i, _ in enumerate(row)})     # enumerate is used to convert it into dictionary
    connection.commit()
    connection.close()
    print("Execution completed Successfully")


def read4(Mobile_id,Brand_Name,Model_Name,RAM,Price):
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from Mobile_Store "

    if Mobile_id != 0:
        sql += "where Mobile_id = " + str(Mobile_id)
    if Brand_Name != '':
        sql += "where Brand_Name like '" + Brand_Name + "%'"
    if Model_Name != '':
        sql += "where Model_Name like '" + Model_Name + "%'"
    if RAM != 0:
        sql += "where RAM = " + str(RAM)
    if Price != 0:
        sql += "where Price = " + str(Price)

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()
    print("Execution completed Successfully")


def read5(Mobile_id,Brand_Name,Model_Name,RAM,Price):
    connection = pymysql.connect(host="localhost", user="root", password="root", db="advpython")
    cursor = connection.cursor()
    sql = "select * from Mobile_Store where 2=2 "     # 2=2  is called as sql injection (it adds two sql queries when we use and instead of where )

    if Mobile_id != 0:
        sql += "and Mobile_id = " + str(Mobile_id)
    if Brand_Name != '':
        sql += "and Brand_Name like '" + Brand_Name + "%'"
    if Model_Name != '':
        sql += "and Model_Name like '" + Model_Name + "%'"
    if RAM != 0:
        sql += "and RAM = " + str(RAM)
    if Price != 0:
        sql += "and Price = " + str(Price)

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()
    print("Execution completed Successfully")


def read6(param={}):
    Mobile_id = param.get('id',0)
    Brand_Name = param.get('Brand_Name','')
    Model_Name = param.get('Model_Name','')
    RAM = param.get('RAM',0)
    Price = param.get('Price',0)
    Page_Size = param.get('Page_Size')
    Page_No = param.get('Page_No')

    connection = pymysql.connect(host="localhost",user="root",password="root",db="advpython")
    cursor = connection.cursor()
    sql = "select * from Mobile_Store where 2=2 "

    if Mobile_id != 0:
        sql += "and Mobile_id =" + str(Mobile_id)
    if Brand_Name != '':
        sql += "and Brand_Name like '" + Brand_Name + "%'"
    if Model_Name != '':
        sql += "and Model_Name like '" + Model_Name + "%'"
    if RAM != 0:
        sql += "and RAM = " + str(RAM)
    if Price != 0:
        sql += "and Price = " +str(Price)

    #pagintation
    if Page_Size > 0:
        offset = (Page_No - 1)* Page_Size
        sql += " limit "+ str(offset) + "," + str(Page_Size)

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()
    print("Execution completed Successfully")


#read1()
#read2()
#read3()
#read4(0,'','',0,130000)
#read5(0,'','',0,18000)
data = {'Mobile_id':0,'Brand_Name':'','Model_Name':'','RAM':0,'Price':20000,'Page_No':3,'Page_Size':4}
read6(data)