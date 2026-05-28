import pymysql
connection = pymysql.connect(host='localhost',user='root',password="root",db="advpython",autocommit=False)
cursor = connection.cursor()
try :
    print("Starting transection...")
    cursor.execute("insert into marksheet values(20,118,'Tushar',56,89,65)" )

    print("Creating Savepoint sp1...")
    cursor.execute("savepoint sp1")

    try:
        cursor.execute("insert into marksheet values(17,117,'Tushar',56,89,65)" )
        print("creating savepoint sp2...")
        cursor.execute("savepoint sp2")

    except Exception as e:
        print("Error in second Insert,rolling back to savepoint1....")
        cursor.execute("rollback to savepoint sp1")

    try:
        cursor.execute("insert into marksheet values(19,119,'Jay',56,89,65)")
        print("Second insert successful..")
        print("Creating savepoint sp3...")
        cursor.execute("savepoint sp3")

    except Exception as e:
        print("Error in third Insert,rolling back to savepoint1....")
        cursor.execute("rollback to savepoint sp1")


    print("Committing Transection...")
    connection.commit()
except Exception as e:
    print("Error in transection.. ",e)
    connection.rollback()

finally:
    cursor.close()
    connection.close()