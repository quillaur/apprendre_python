from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    
    return key


def load_key():
    with open("key.key", "rb") as f:
        key = f.read()
    
    return key


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            user, passw = line.strip().split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Nom de compte: ")
    pwd = input("MDP: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


if __name__ == '__main__':

    if not os.path.exists("key.key"):
        write_key()

    key = load_key()
    fer = Fernet(key)

    while True:
        mode = input(
            """
            Que veux tu faire ?
            - Ecris 'ajouter' pour ajouter un nouveau mdp.
            - Ecris 'voir' pour voir l'ensemble de la base de données.
            - Appuis sur q pour quitter. 
            """).lower()
        
        if mode == "q":
            break

        if mode == "voir":
            view()
        elif mode == "ajouter":
            add()
        else:
            print("La réponse donnée n'est pas correcte.")
            continue