import pymysql

class Marksheet_Model:

    def next_Primary_Key(self):
        Primary_Key = 0
        connection = pymysql.connect(host='localhost', user='root', password='root', db='advpython')
        cursor = connection.cursor()
        sql = "select max(id) from marksheet "
        cursor.execute(sql)
        data = cursor.fetchone()
        if data[0] is not None:
            Primary_Key = data[0]
        connection.commit()
        connection.close()
        return Primary_Key + 1


    def insert(self,data):
        id = data['id']
        roll_no =data['roll_no']
        name = data['name']
        phy = data['phy']
        che = data['che']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', user='root', password='root', db='advpython')
        cursor = connection.cursor()
        sql = "insert into marksheet values(%s,%s,%s,%s,%s,%s)"
        #result = (id,roll_no,name,phy,che,maths)
        cursor.execute(sql,(id,roll_no,name,phy,che,maths))
        connection.commit()
        connection.close()
        print("Data inserted successfully...")


    def update(self,data):
        id = data['id']
        roll_no = data['roll_no']
        name = data['name']
        phy = data['phy']
        che = data['che']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', user='root', password='root', db='advpython')
        cursor = connection.cursor()
        sql = "update marksheet set roll_no = %s,name= %s,phy=%s,che=%s,maths=%s where id = %s"
        cursor.execute(sql,(roll_no,name,phy,che,maths,id))
        connection.commit()
        connection.close()
        print("Data Updated successfully...")


    def delete(self,id):
        connection = pymysql.connect(host='localhost', user='root', password='root', db='advpython')
        cursor = connection.cursor()
        sql = "delete from marksheet where id = %s"
        cursor.execute(sql,id)
        connection.commit()
        connection.close()
        print("Data Deleted successfully..")


    def get(self,id):
        connection = pymysql.connect(host='localhost', user='root', password='root', db='advpython')
        cursor = connection.cursor()
        sql = "select * from marksheet where id = %s "
        cursor.execute(sql,id)
        data = cursor.fetchall()
        for row in data:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t')
        connection.commit()
        connection.close()
        print("Data Get successfully..")


    def Find_by_roll(self,roll_no):
        connection = pymysql.connect(host='localhost', user='root', password='root', db='advpython')
        cursor = connection.cursor()
        sql = "select * from marksheet where roll_no = %s "
        cursor.execute(sql,roll_no)
        data = cursor.fetchall()
        for row in data:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t')
        connection.commit()
        connection.close()
        print("Data Get successfully..")


    def search(self,data):
        id = data['id']
        roll_no = data['roll_no']
        name = data['name']
        phy = data['phy']
        che = data['che']
        maths = data['maths']
        page_no = data['page_no']
        page_size = data['page_size']
        connection = pymysql.connect(host='localhost', user='root', password='root', db='advpython')
        cursor = connection.cursor()
        sql = "select * from marksheet where 1=1 " #sql injection

        if id != 0:
            sql += "and id = "+str(id)
        if roll_no != 0:
            sql += "and roll_no = "+str(roll_no)
        if name != '':
            sql += "and name like '" + name + "%'"
        if phy != 0:
            sql += "and phy = "+str(phy)
        if che != 0:
            sql += "and che = "+str(che)
        if maths != 0:
            sql += "and maths = "+str(maths)

        if page_size > 0:
            offset = (page_no - 1)*page_size
            sql += " limit "+str(offset)+","+str(page_size)

        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\t',row[5],'\t')
        connection.commit()
        connection.close()
        print("Data Searched successfully..")