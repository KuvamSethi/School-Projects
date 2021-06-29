"""
! ~~~~~~~~ PYTHON CLIENT DATA MANAGEMENT SYSTEM ~~~~~~~~

?-> This is a program for a gym to maintain its trainer and client details and their progress.
?-> The program helps to keep different files for each client and also prevent name overlapping.
?-> The program keeps a record of food and excercise done/eaten by the client.

Trivia:
    -> Created: 20-06-21 ; Latest Update: 22-06-21
    -> The program is written in Python File I/O.
    -> Author: Harshit Singh (GitHub: HarshitSingh-Code Link: https://github.com/HarshitSingh-Code)

//TODO(1.0): -> Add automatic name generator 
//TODO(1.1): -> Add username and password login for each user
TODO(1.2): -> Revamp the app from File I/O to Pickle I/O 
TODO(1.3): -> Add trainer signup 
TODO(1.4): -> Complete the login system and after features 

"""

# * 🚢 Import Statements
import time
import random as rd
import getpass
import os

# * 🎁 Function Declarations

# 🎯 Data Logging - Function
def log(name):
    # using File I/O
    with open(f"{name}_{mode}.txt", "a") as file:
        while True:
            # Asking user what he did
            DID = int(
                input("\nWhat to Log ?\n1.) Food\n2.) Excercise\nEnter the respective no. : "))
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
    with open(f"{name}.txt", "a+") as file:
        file.seek(0)
        if file.read() == "":
            print("\nPlease log something before you retrieve.\n")
        else:
            file.seek(0)
            print(f"\n{file.read()}")

# 🙆 Clients List - Function
def clientList(mode):
    with open(f"{mode}_list.txt", "a+") as file:
        file.seek(0)
        return file.readlines()

# ☂️ Numbered list (mode) - Function
def numeratedList(mode):
    num_list = clientList(mode)
    return [f"{key+1}.) {value.split('|')[0]}" for key, value in enumerate(num_list)]

# 🆕 Add new Client - Function
def addClient(name, passw, mode):
    with open(f"{mode}_list.txt", "a+") as file:
        file.write(f"{name}|{passw}\n") 

# 🤺 Check Client present - Function
def checkName(name, mode):
    if f"{name}" in [x.split("|")[0] for x in clientList(mode)]:
        return True
    else:
        return False

# 🧮 Check Login Information - Function
def checkInfo(name, passd, mode):
        clients_details = clientList(mode)
        details = {}
        for detail in clients_details:
            user, passw = detail.split("|")
            details[user] = passw
        if name in details.keys():
            if details[name] == passd+"\n":
                return [True, "Login Successful."]
            else:
                return [False, "Incorrect Password."]
        else:
            return [False, "Incorrect Username."]

# 🎰 Automatic name Generator - Function
def nameGen(name, mode):
    name = name.split("#")[0]
    while True:
        rand = round(rd.random()*(10**4))
        sug_name = f"{name}#{rand}"
        if checkName(sug_name, mode):  # checking the name availability
            continue
        else:
            return sug_name

# * Main Code Starts here 👇

if __name__ == "__main__":
    # while loop for re-running tasks so that user don't have to run repeadtely,
    #  to do different tasks.🔻
    while True:
        run = input("\nEnter :\n1.) Run\n2.) Exit\nEnter the respective no. : ")
        if run == "1":
            while True:
                dashboard = input(
                    "\nWhat to do?\n1.) Login\n2.) Sign Up\n3.) Exit\nEnter the respective no. : ")
                while True:
                    who = input(
                        "\nWho are you ?\n1.) Client\n2.) Trainer\n3.) Go back\nEnter the respective no. : ")
                    if who == "1":
                        mode = "client"
                    elif who == "2":
                        mode = "trainer"
                    elif who == "3":
                        break
                    else:
                        print("Invalid input! Please try again.")
                        continue
                    username = input("\nUsername: ")
                    password = getpass.getpass(prompt="Password: ")
                    if dashboard == "1":
                        while not checkInfo(username, password, mode)[0]:
                            ask = input("\nPress 1 to Go back and 2 to continue : ")
                            if ask == "1":
                                break
                            elif ask == "2":
                                if checkInfo(username, password, mode)[1] == "Incorrect Password.":
                                    password = getpass.getpass(
                                        prompt=f"\n{checkInfo(username, password, mode)[1]} Re-enter Password : ")
                                    continue
                                else:
                                    print(f"\n{checkInfo(username, password, mode)[1]} Re-enter Username and Password.")
                                    username = input("\nUsername: ")
                                    password = getpass.getpass(prompt="Password: ")
                                    continue
                        break
                        welcome_msg = f"{checkInfo(username, password, mode)[1]} Welcome {mode[0].upper()+mode[1:].lower()} {username}"
                        print()
                        print("~"*len(welcome_msg))
                        print(welcome_msg)
                        print("~"*len(welcome_msg))
                        if mode == "client":
                            # 📢 Asking the Client if he wants to log or retrieve data
                            DO = input(
                                "\nWhat you want to do ?\n1.) Log\n2.) Retrieve\nEnter the respective no. : ")
                            if DO == "1":
                                # logging function
                                log(username, mode)
                                rev(username, mode)
                            elif DO == "2":
                                # retrieving function
                                rev(username, mode)
                            continue
                        #TODO(1.4) -> Goes Here !
                    elif dashboard == "2":
                        re_pass = getpass.getpass(prompt="Confirm password : ")
                        while checkName(username, mode):
                            gen_name = nameGen(username, mode)
                            print(f"\nUsername already taken. You can use {gen_name}")
                            username = input("Try a different username or enter 1 to use the suggested  : ")
                            if username == "1":
                                username = gen_name
                                break
                        while re_pass != password:
                            print("Password didn't match.")
                            password = getpass.getpass(prompt="Re-enter password : ")
                            re_pass = getpass.getpass(prompt="Re-enter confirm password : ")
                        addClient(username, password, mode)
                        welcome_msg = f"SignUp successful. Welcome {mode[0].upper() + mode[1:].lower()} {username}"
                        print()
                        print("~"*len(welcome_msg))
                        print(welcome_msg)
                        print("~"*len(welcome_msg))
                        if mode == "client" and os.path.isfile("trainer_list.txt"):
                            pr_trainer = input(f"\nChoose your personal trainer\n{chr(10).join(numeratedList('trainer'))}\nEnter the respective no. : ")
                            choose = f"You Choosed {numeratedList('trainer')[int(pr_trainer)-1].split(' ')[1]} as your trainer."
                            print()
                            print("~"*len(choose))
                            print(choose)
                            print("~"*len(choose))
                        #TODO(1.3) -> Goes Here !
                        break                
                    elif dashboard == "3":
                        print("\nThank you for using our data management system.")
                        exit(0)
        elif run == "2":
            print("\nThank you for using our data management system.")
            exit(0)
        else:
            print("\nInvalid input! Please try again.")
            continue
