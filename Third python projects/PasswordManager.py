from cryptography.fernet import Fernet

"""
def write_key():
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
                key_file.write(key) 
"""

master_pass = input("Enter the master password (be sure to remember it): ")

def load_key():
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key

key = load_key() 
fer = Fernet(key)


def view():
    with open('password_database.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw, phoneN = data.split("|")
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode(), "| Phone Number:", fer.decrypt(phoneN.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    phone = input("Phone number: ")
    
    with open('password_database.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "|" + fer.encrypt(phone.encode()).decode() + "\n")


while True:
    mode = input("View or add a password (v/a) or q to quit?: ")
    mode.lower()
    if mode == "q":
            break
        
    if mode == "v":
        while True:
                userInput = input("Enter the master password before viewing information")
                if userInput == master_pass:
                        break
                elif userInput == "q":
                        quit()
                else:
                        print("Sorry that password is incorrect, try again or press q to quit")
                        continue
        view()
    elif mode == "a":
        while True:
                userInput = input("Enter the master password before adding information")
                if userInput == master_pass:
                        break
                elif userInput == "q":
                        quit()
                else:
                        print("Sorry that password is incorrect, try again or press q to quit")
                        continue
        add()
    else:
        print("Invalid input")
        continue
        
