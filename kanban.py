from init import *
from prettytable import PrettyTable
from colorama import Fore
import time

def showmenu():
    time.sleep(0.5)
    print("\n")
    print(Fore.LIGHTMAGENTA_EX+"1.View Kanban\n2.Add task\n3.Move tasks\n4.Delete task\n5.Quit")
    
def show_tasks(status):
  command = f"select Taskname,Priority,Reportee,Assignee from Kanban_table where Status ='{status}' order by Priority"
  cursor.execute(command)
  data = cursor.fetchall()
  if(data):
      ptable = PrettyTable(["Taskname","Priority","Reportee","Assignee"])
      for a,b,c,d in data:
          ptable.add_row([a,b,c,d])
      print(ptable)
  else:
      print("-----Empty-----")

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
    
        print(Fore.RED+"________𝗧𝗢-𝗗𝗢________")
        show_tasks("To-Do")
        

        print(Fore.YELLOW+"________𝗜𝗡-𝗣𝗥𝗢𝗚𝗥𝗘𝗦𝗦________")
        show_tasks("In-Progress")

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
    if not isempty():
        tasknames = PrettyTable(["Task names","Status"])
        cursor.execute("select Taskname,Status from Kanban_table")
        data = cursor.fetchall()
        for a,b in data:
            tasknames.add_row([a,b])
        print(tasknames)
        task = input("Enter task name: ")
        movelocation = input("Enter new status of task (To-do,In-progress,Done): ")
        cursor.execute("update kanban_table set status = '{}' where taskname = '{}'".format(movelocation,task))
        mycon.commit()
    else:
        print("No tasks present")

def deltask():
    if not isempty():
        tasknames = PrettyTable(["Task names","Status"])
        cursor.execute("select Taskname,Status from Kanban_table")
        data = cursor.fetchall()
        for a,b in data:
            tasknames.add_row([a,b])
        print(tasknames)
        task = input("Enter task name: ")
        confirm = input(Fore.RED+"Confirm deletion (y/n): ")
        if (confirm=='y'):
            cursor.execute("delete from kanban_table where taskname = '{}' ".format(task))
            mycon.commit()
            print(Fore.LIGHTYELLOW_EX)
    else:
        print("No tasks present")

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
    print(Fore.RED+"Exiting...")
    print(Fore.WHITE)
    quit()
