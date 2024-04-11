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
        cursor.execute("INSERT INTO Kanban_Table (Taskname,Status,Priority, Reportee, Assignee) VALUES ('{}','{}',{},'{}','{}');".format(taskname,status,priority,reportee,assignee))

def displaykanban():
    if isempty():
        print("No tasks present,Please add some tasks.")
        rows = int(input("How many tasks would you like to add?"))
        addrows(rows)
    else:
        #Print entire Kanban table
        print(PrettyTable(["To-Do"]))
        ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
        cursor.execute("select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='To-do' order by Priority")
        data = cursor.fetchall()
        if(data):
            for a,b,c,d in data:
                ptable.add_row([a,b,c,d])
            print(ptable)
        else:
            print("Empty")
        print("\n")

        print(PrettyTable(["In-Progress"]))
        ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
        cursor.execute("select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='In-progress' order by Priority")
        data = cursor.fetchall()
        if(data):
            for a,b,c,d in data:
                ptable.add_row([a,b,c,d])
            print(ptable)
        else:
            print("Empty")
        print("\n")

        print(PrettyTable(["Done"]))
        ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
        cursor.execute("select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='Done' order by Priority")
        data = cursor.fetchall()
        if(data):
            for a,b,c,d in data:
                ptable.add_row([a,b,c,d])
            print(ptable)
        else:
            print("Empty")

def main():
    while(True):
        print("1.View Kanban\n2.Add tasks\n3.Move tasks\n4.Delete task\n5.Quit")
        inp = int(input("Enter a choice corresponding to number: "))
        if(inp==1):
            displaykanban()
        if(inp==2):
            addrows(1)
        if(inp==3):
            inp = 2
        if(inp==4):
            inp = 3
        if(inp==5):
            mycon.commit()
            mycon.close()
            quit()


initialization()
main()

