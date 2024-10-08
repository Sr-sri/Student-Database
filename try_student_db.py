# check_attendance.py
import mysql.connector


con = mysql.connector.connect(host='localhost', user='root', password='JSkc11@*', database='dsce')
res = con.cursor()

def ai_data(id):
    sql = '''
    SELECT regno, name, deptname
    FROM students_students
    WHERE regno = %s
    '''
    data = (int(id),)
    res.execute(sql, data)
    result = res.fetchone()
    return result

def others_data(data):
    sql="insert into students_others_dept (regno) values (%s)"
    data=(int(data),)
    res.execute(sql,data)
    con.commit()
    result=res.fetchone()
    return result


     
