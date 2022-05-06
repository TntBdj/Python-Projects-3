from unicodedata import name
from cryptography.fernet import Fernet

master_pass = input("Enter the master password (be sure to remember it): ")

def new_key():
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key

key = new_key() 
fer = Fernet(key)


def add_info():
    name = input("Account name: ")
    pwd = input("Password: ")
    phone = input("Phone number: ")
    
    with open('password_database.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "|" + fer.encrypt(phone.encode()).decode() + "\n")


def view_info():
    with open('password_database.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                name, password, phoneNumber = data.split("|")
                print("Name:", name, "| Password:", fer.decrypt(password.encode()).decode(), "| Phone Number:", fer.decrypt(phoneNumber.encode()).decode())


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
        
