import re                                               #importing libraries
print("Welcome to the Calculator.")
print("Type 'Q' to exit.\n")

previous = 0                                              #Used to hold the older value
run = True                                                #used for looping a calculator

def operation():
    global run
    global previous
    equation = ""
    if previous == 0:                                      #checks if starting value is 0 or not
        equation = input("Enter your equation:")           #input
    else:
        equation = input(str(previous))                    #if previous value is not 0, prints previous value



    if equation == "Q" or equation == 'q':                                 #check if user wants to quit
        print("Thank You")
        run == false                                       #exit the loop

    else:
        equation = re.sub('[A-Za-z,.\':;" "]','',equation) #re.sub() is built in func. to replace specific characters from string
        if previous == 0:
            previous = eval(equation)                      #eval() is a built in func. used to evaluate a string
        else:
            previous = eval(str(previous) + equation )
            print(previous)

while run: #loop will continue till run is false
    operation()