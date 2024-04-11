import mysql.connector as sqltor
from prettytable import PrettyTable
import time
from colorama import Fore

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
        print("________𝗧𝗢-𝗗𝗢________")
        ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
        cursor.execute("select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='To-do' order by Priority")
        data = cursor.fetchall()
        if(data):
            for a,b,c,d in data:
                ptable.add_row([a,b,c,d])
            print(ptable)
        else:
            print("-----Empty-----")
        

        print("________𝗜𝗡-𝗣𝗥𝗢𝗚𝗥𝗘𝗦𝗦________")
        ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
        cursor.execute("select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='In-progress' order by Priority")
        data = cursor.fetchall()
        if(data):
            for a,b,c,d in data:
                ptable.add_row([a,b,c,d])
            print(ptable)
        else:
            print("-----Empty-----") 

        print("________𝗗𝗢𝗡𝗘________")
        ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
        cursor.execute("select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='Done' order by Priority")
        data = cursor.fetchall()
        if(data):
            for a,b,c,d in data:
                ptable.add_row([a,b,c,d])
            print(ptable)
        else:
            print("-----Empty-----")
        print("\n\n")

def movetask():
    task = input("Enter task name: ")
    movelocation = input("Enter new status of task (To-do,In-progress,Done): ")
    cursor.execute("update kanban_table set status = '{}' where taskname = '{}'".format(movelocation,task))
    mycon.commit()

def deltask():
    task = input("Enter task name")
    confirm = input("Confirm deletion (y/n): ")
    if (confirm=='y'):
        cursor.execute("delete from kanban_table where taskname = '{}' ".format(task))
        mycon.commit()

def main():
    #HIT ZERO TO RESET THE PROGRAM
    while(True):
        time.sleep(0.5)
        print("\n")
        print("1.View Kanban\n2.Add tasks\n3.Move tasks\n4.Delete task\n5.Quit")
        inp = int(input("Enter a choice corresponding to number: "))
        if(inp==0):
            c = input("Confirm reset (y/n): ")
            if(c=='y'):
                cursor.execute("drop table Kanban_table")
                cursor.execute("drop database kanban")
                mycon.commit()
                mycon.close()
                print("__________RESET__________")
                quit()
                
            else:
                continue
        elif(inp==1):
            displaykanban()

        elif(inp==2):
            addrows(1)

        elif(inp==3):
            movetask()

        elif(inp==4):
            deltask()
            
        elif(inp==5):
            mycon.commit()
            mycon.close()
            quit()


#initialization()
#main()


