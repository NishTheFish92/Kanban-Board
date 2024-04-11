import mysql.connector as sqltor
from prettytable import PrettyTable
mycon = sqltor.connect(host ='localhost',user = 'root',passwd = 'root@123')
cursor = mycon.cursor()
def initialization():
    cursor.execute("create database IF NOT EXISTS Kanban")
    cursor.execute("use Kanban")
    cursor.execute("CREATE TABLE IF NOT EXISTS Kanban_Table (Taskname VARCHAR(255),Status VARCHAR(50),Priority INT,Reportee VARCHAR(100),Assignee VARCHAR(100));")

def isempty():
    cursor.execute("select * from Kanban_Table;")
    data = cursor.fetchall()
    if(not data):
        return 1
    else:
        return 0
def addrows(x):
    for i in range(x):
        taskname = input("Enter taskname: ")
        status = input("Enter status (To-do,In-progress,Done): ")
        priority = int(input("Enter priority rank (1 highest,3 lowest): "))
        reportee = input("Enter reportee: ")
        assignee = input("Enter assignee: ")
        cursor.execute("INSERT INTO Kanban_Table (Taskname, Taskdesc, Status,Priority, Reportee, Assignee) VALUES ({},{},{},{},{})".format(taskname,status,priority,reportee,assignee))

def displaykanban():
    if isempty():
        print("No tasks present,Please add some tasks.")
        rows = int(input("How many tasks would you like to add?"))
        addrows(rows)
    else:
        #Print entire Kanban table
mycon.close()
