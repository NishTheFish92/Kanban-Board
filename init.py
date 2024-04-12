import mysql.connector as sqltor
mycon = sqltor.connect(host ='localhost',user = 'root',passwd = 'root@123')
cursor = mycon.cursor()
def initialization():
    cursor.execute("create database IF NOT EXISTS Kanban")
    cursor.execute("use Kanban")
    cursor.execute("CREATE TABLE IF NOT EXISTS Kanban_Table (Taskname VARCHAR(255),Status VARCHAR(50),Priority INT,Reportee VARCHAR(100),Assignee VARCHAR(100));")