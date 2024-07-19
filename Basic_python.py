# File: apply example
#TODO
#{*} Print to terminal
#{*} Create user selections
#{*} Use basic math
#{*} Allow Multiple calcuations without closing script
#{*} create a basic calculator script
#{*} create a calculator script that can save the last answer to use on the next iteration
#{} clean code to make script cleaner
import sys
import os

print("Welcome to Math")
print("press q to quit at anytime")
userop = "0"
runcounter = 0
#a = sys.stdin.readline() #Waits for User String
#print(a) # Reprints the user's string showing completion to the convertion
while True:
    runcounter = runcounter + 1
    print ("Enter the first number")
    #take user input from terminal and strip extra space from input
    userinput1 = sys.stdin.readline().strip(

    )
    #check user input for q to leave while loop
    if userinput1 == "q":
            break
    elif userinput1 == "r" and runcounter >= 1:
        try:
              #Check that the userinput is an integer
            print ("Enter the second number")
            userinput2 = sys.stdin.readline().strip(

            ) 
        
        except:
            print("Sorry you must enter a valid integer")
            
        if userinput2 == "q":
           break
        else:
            try:
                userchoice = usersave   
                int(userinput2)
                print("Please select operation + for addition - for substration * for multiplicationn / for division or Q to quit" )
                userop = sys.stdin.readline().strip(

                    )
                print(userop)
                    # Note the input from the terminal is a string data type. must force to integer to proper
                    # compute the operation
                if userop == "+":
                    temp = int(userchoice) + int(userinput2)
                elif userop == "-":
                    temp = int(userchoice) - int(userinput2)
                elif userop == "*":
                    temp = int(userchoice) * int(userinput2)
                elif userop == "/":
                    temp = (int(userchoice) / int(userinput2)) 
                elif userop == "q":
                    break
                else:
                    temp = "Caclulation Failed"
                print(temp)
                usersave = temp 
            except:
                print("An Error has occured")
    else:
        try:
            #Check that the userinput is an integer
            int(userinput1)
            print ("Enter the second number")
            userinput2 = sys.stdin.readline().strip(

            ) 
        
        except:
            print("Sorry you must enter a valid integer")
            
        if userinput2 == "q":
           break
        else:
            try:
                int(userinput2)
                print("Please select operation + for addition - for substration * for multiplicationn / for division or Q to quit" )
                userop = sys.stdin.readline().strip(

                    )
                print(userop)
                    # Note the input from the terminal is a string data type. must force to integer to proper
                    # compute the operation
                if userop == "+":
                    temp = int(userinput1) + int(userinput2)
                elif userop == "-":
                    temp = int(userinput1) - int(userinput2)
                elif userop == "*":
                    temp = int(userinput1) * int(userinput2)
                elif userop == "/":
                    temp = (int(userinput1) / int(userinput2)) 
                elif userop == "q":
                    break
                else:
                    temp = "Caclulation Failed"
                print(temp)
                usersave = temp 
            except:
                print("Sorry you must enter a valid integer")
            
               
              

