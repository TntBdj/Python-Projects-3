from cryptography.fernet import Fernet

"""
def write_key():
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
                key_file.write(key) 
"""

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
            view()
    elif mode == "a":
            add()
    else:
        print("Invalid input")
        continue
        