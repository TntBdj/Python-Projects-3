#Imported modules for running the file
from unicodedata import name
from cryptography.fernet import Fernet

#The master password that muct be remembered to do any functions
master_pass = input("Enter the master password (be sure to remember it): ")

def new_key():
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key

key = new_key() 
fer = Fernet(key)

#Allows the user to add information onto their encrypted file
def add_info():
    name = input("Account name: ")
    pwd = input("Password: ")
    phone = input("Phone number: ")
    
    with open('password_database.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "|" + fer.encrypt(phone.encode()).decode() + "\n")

#Allows the user to view information on their encrypted file
def view_info():
    with open('password_database.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                name, password, phoneNumber = data.split("|")
                print("Name:", name, "| Password:", fer.decrypt(password.encode()).decode(), "| Phone Number:", fer.decrypt(phoneNumber.encode()).decode())

#This will ask the user if they want to add or view information, then to input the master password, or simply quit
while True:
    userSelection = input("View or add a password (v/a) or q to quit?: ")
    userSelection.lower()
    if userSelection == "q":
            break
    elif userSelection == "v":
        while True:
                userInput = input("Enter the master password before viewing information: ")
                if userInput == master_pass:
                        break
                elif userInput == "q":
                        quit()
                else:
                        print("Sorry that password is incorrect, try again or press q to quit")
                        continue
        view_info()
    elif userSelection == "a":
        while True:
                userInput = input("Enter the master password before adding information: ")
                if userInput == master_pass:
                        break
                elif userInput == "q":
                        quit()
                else:
                        print("Sorry that password is incorrect, try again or press q to quit")
                        continue
        add_info()
    else:
        print("Invalid input")
        continue
        
