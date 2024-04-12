from init import *
from prettytable import PrettyTable
from colorama import Fore
import time

def showmenu():
    time.sleep(0.5)
    print("\n")
    print(Fore.LIGHTMAGENTA_EX+"1.View Kanban\n2.Add task\n3.Move tasks\n4.Delete task\n5.Quit")
    

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
        choice = input("No tasks present,Would you like to add some?(y/n) ")
        if choice=='y':
            rows = int(input("How many tasks would you like to add?"))
            addrows(rows)
    else:
        #Print entire Kanban table
        print(Fore.RED+"________𝗧𝗢-𝗗𝗢________")
        ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
        cursor.execute("select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='To-do' order by Priority")
        data = cursor.fetchall()
        if(data):
            for a,b,c,d in data:
                ptable.add_row([a,b,c,d])
            print(ptable)
        else:
            print("-----Empty-----")
        

        print(Fore.YELLOW+"________𝗜𝗡-𝗣𝗥𝗢𝗚𝗥𝗘𝗦𝗦________")
        ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
        cursor.execute("select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='In-progress' order by Priority")
        data = cursor.fetchall()
        if(data):
            for a,b,c,d in data:
                ptable.add_row([a,b,c,d])
            print(ptable)
        else:
            print("-----Empty-----") 

        print(Fore.GREEN+"________𝗗𝗢𝗡𝗘________")
        ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
        cursor.execute("select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='Done' order by Priority")
        data = cursor.fetchall()
        if(data):
            for a,b,c,d in data:
                ptable.add_row([a,b,c,d])
            print(ptable)
        else:
            print("-----Empty-----")

def movetask():
    task = input("Enter task name: ")
    movelocation = input("Enter new status of task (To-do,In-progress,Done): ")
    cursor.execute("update kanban_table set status = '{}' where taskname = '{}'".format(movelocation,task))
    mycon.commit()

def deltask():
    task = input("Enter task name: ")
    confirm = input("Confirm deletion (y/n): ")
    if (confirm=='y'):
        cursor.execute("delete from kanban_table where taskname = '{}' ".format(task))
        mycon.commit()

def reset():
    c = input(Fore.RED+"Confirm reset (y/n): ")
    if(c=='y'):
        cursor.execute("drop table Kanban_table")
        cursor.execute("drop database kanban")
        mycon.commit()
        mycon.close()
        print("__________RESET__________")
        print(Fore.WHITE)
        quit()

def quitkanban():
    mycon.commit()
    mycon.close()
    print(Fore.WHITE)
    quit()
