import mysql.connector
import datetime

con = mysql.connector.connect(host='localhost', user='root', password='JSkc11@*', database='dsce')
res = con.cursor()
 


def count_fun():
          
    sql='SELECT COUNT(*) FROM students_all_depts'
    res.execute(sql)
    total_count=res.fetchone()
    total=total_count[0]
    print(total)

count_fun()

