from init import *
from kanban import *

def main():

    while(True):

        showmenu()
        inp = int(input(Fore.LIGHTYELLOW_EX+"Enter a choice corresponding to number: "))

        if(inp==0):
            reset()

        elif(inp==1):
            displaykanban()

        elif(inp==2):
            addrows(1)

        elif(inp==3):
            movetask()

        elif(inp==4):
            deltask()
            
        elif(inp==5):
            quitkanban()


initialization()
main()