import time

class Astronaught():
    name = None
    color = None

    def __init__(self, name, color):
        self.name = name
        self.color = color

    taskMath = False     # word problem!
    taskO2 = False       # waiting!
    taskValidate = False # password!

    def MathTask(self):
        print()
        print("Our space station needs to be 100 miles")
        print("farther than we are now. How fast do we")
        print("need to go to be there in 20 minutes?")
        print("(answer in miles per minute)")
        if input("> ") == '5':
            print("Correct. Well done!")
            self.taskMath = True
        else:
            print("Incorrect. Please try again.")
        print()
    
    def O2Task(self):
        print()
        print("F - Fill Tanks")
        print("B - Back")
        print()
        o2choice = input("> ")
        if o2choice == 'F':
            print("Filling... 0%")
            time.sleep(1)
            print()
            print("Filling... 15%")
            time.sleep(.9)
            print()
            print("Filling... 42%")
            time.sleep(1.3)
            print()
            print("Filling... 87%")
            time.sleep(.5)
            print()
            print("Filling... 96%")
            time.sleep(.5)
            print()
            print("Filling... 97%")
            time.sleep(.5)
            print()
            print("Filling... 98%")
            time.sleep(.5)
            print()
            print("Filling... 99%")
            time.sleep(.5)
            print()
            print("Filling... 100%")
            time.sleep(1)
            print("Filling Complete!")
            self.taskO2 = True
        print()
    
    def Validate(self):
        print()
        print("Crew Member:", self.name)
        colorIn = input("Please input your color: ")
        print()
        if colorIn == self.color:
            print("Crew Member Validated")
            self.taskValidate = True
        else:
            print("Incorrect. Please try again.")
        print()

# Start here! :)
print("\033[1;37;40m")
print("Context: You are an astronaught!")
print("You have a few tasks you need to complete.")
print("Complete the tasks, and you win!")
print()
player = Astronaught(input("Name: "), input("Color: "))
print()

choice = None
while choice != 'S':
    # show tasks
    if player.taskMath == True:
        print("1 -\033[1;32;40m Complete \033[1;37;40m- Destination")
    else:
        print("1 -\033[1;31;40m Incomplete \033[1;37;40m- Destination")

    if player.taskO2 == True:
        print("2 -\033[1;32;40m Complete \033[1;37;40m- Oxygen")
    else:
        print("2 -\033[1;31;40m Incomplete \033[1;37;40m- Oxygen")
    
    if player.taskValidate == True:
        print("3 -\033[1;32;40m Complete \033[1;37;40m- Validation")
    else:
        print("3 -\033[1;31;40m Incomplete \033[1;37;40m- Validation")
    print("S - Submit")
    print()

    # choices
    choice = input("> ")
    if choice == '1':
        player.MathTask()
    elif choice == '2':
        player.O2Task()
    elif choice == '3':
        player.Validate()

if player.taskMath and player.taskO2 and player.taskValidate:
    print("All Tasks Complete. Thanks for playing!")
else:
    print("Tasks Incomplete. Please play again!")

