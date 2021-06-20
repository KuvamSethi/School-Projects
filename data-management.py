"""
! ~~~~~~~~ PYTHON CLIENT DATA MANAGEMENT SYSTEM ~~~~~~~~

?-> This is a program for a gym to maintain his/her client details and their progress.
?-> The program helps to keep different files for each client and also prevent name overlapping.
?-> The program keeps a record of food and excercise done/eaten by the client.

Trivia:
    -> The program is written in Python File I/O.
    -> Author: Harshit Singh (GitHub: HarshitSingh-Code Link: https://github.com/HarshitSingh-Code)

TODO(1.0): -> Add automatic name generator 
TODO(1.1): -> Add username and password login for each user
    
"""

#* 🚢 Import Statements 
import time
import random as rd

#* 🎁 Function Declarations

# 🎯 Data Logging - Function
def log(name):
    # using File I/O
    with open(f"{name}.txt", "a") as file:
        while True:
            # Asking user what he did
            DID = int(input("\nWhat to Log ?\n1.) Food\n2.) Excercise\nEnter the respective no. : "))
            if DID == 1:
                food = input("\nWhat meal did you had : ")
                print()
                file.write(f'{time.asctime()} : Food -> {food}\n')
                break
            elif DID == 2:
                excer = input("\nWhat excercise you did : ")
                print()
                file.write(f'{time.asctime()} : Excercise -> {excer}\n')
                break
            else:
                print("Something went wrong!")
                continue

# 📅 Data Retrival - Function 
def rev(name):
    with open(f"{name}.txt") as file:
        file.seek(0)
        if file.read() == "":
            print("\nPlease log something before you retrieve.\n")
        else:
            file.seek(0)
            print(f"\n{file.read()}")

# 🙆 Clients List - Function 
def clientList(name):
    with open("client_list.txt", "a+") as file:
        file.seek(0)
        return file.readlines()

# 🆕 Add new Client - Function 
def addClient(name):
    with open("client_list.txt", "a+") as file:
        file.write(f"{name}\n")

# 🤺 Check Client present - Function 
def checkName(name):
    if f"{name}\n" in clientList(name):
        return True
    else:
        return False

# 🎰 Automatic name Generator - Function
def nameGen(name):
    rand = round(rd.random()*(10**4))
    return f"{name}#{rand}"

#* Main Code Starts here 👇

if __name__ == "__main__":
    # while loop for re-running tasks so that user don't have to run repeadtely,
    #  to do different tasks.🔻
    while True:
        # variable + conditons to exit the big brain loop.
        run = int(input("Enter 1 to run and 0 to exit : "))
        if run == 1:
            # 🧑‍🤝‍🧑 Client name input 
            NAME = input("\nEnter your name to log : ")
            new_client = input("Are you a new client (y/n) : ")
            # ✅ Checking if client is new and isn't using the same username as other.
            if new_client in "Yy":
                while checkName(NAME):
                    genName = nameGen(NAME)
                    print(f"\nThis name is already taken, you can use {genName}.")
                    NAME = input("Please try a different name, You can enter 1 to use suggested name : ")
                    if NAME == "1":
                        NAME = genName
                    else:
                        print("Invalid input please enter again.")
                        continue

                addClient(NAME)
            # ✅ Checking if client is old and enters with correct username.
            elif new_client in "Nn":
                 while not checkName(NAME):
                    NAME = input("No existing Client with this name. Please enter correctly : ")
            else:
                print("Not a valid option! Please try again.")
                continue
            # 📢 Asking the Client if he wants to log or retrieve data
            DO = int(input("\nWhat you want to do ?\n1.) Log\n2.) Retrieve\nEnter the respective no. : "))
            if DO == 1:
                # logging function 
                log(NAME)
                rev(NAME)
            elif DO == 2:
                # retrieving function 
                rev(NAME)
            continue
        elif run == 0:
            # ⚔️ Code exit
            print("\nThank you for using our Data Management System.")
            break
        else:
            print("Please input valid values!")
            continue