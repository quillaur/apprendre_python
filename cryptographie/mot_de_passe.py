from cryptography.fernet import Fernet
import os

# Le but est de stocker des identifiants et mots de passes dans un fichier.
# Afin que le fichier ne soit accessible que par l'utilisateur,
# le fichier sera encrypté grâce au module cryptography.

def write_key() -> str:
    """
    Fonction permettant de générer une clef de cryptographie
    et de la sauvegarder dans un fichier local.

    Return:
        La clef.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    
    return key


def load_key() -> str:
    """
    Fonction permettant de charger une clef de cryptographie 
    sauvegarder au préalable dans le fichier key.key.

    Return:
        La clef.
    """
    with open("key.key", "rb") as f:
        key = f.read()
    
    return key


def view() -> None:
    """
    Méthode pour voir les identifiants / mots de passes stockés dans passwords.txt.
    """
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            user, passw = line.strip().split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add() -> None:
    """
    Méthode pour écrires les identifiants / mots de passes dans passwords.txt.
    """
    name = input("Nom de compte: ")
    pwd = input("MDP: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


if __name__ == '__main__':

    # Si nous n'avons jamais créé la clef,
    # alors il faut la générer et la sauvegarder dans un fichier.
    if not os.path.exists("key.key"):
        write_key()

    # Chargeons la clef.
    key = load_key()

    # On insère notre clef dans l'algorithme de cryptographie.
    fer = Fernet(key)

    # Tant que l'utilisateur veut intéragir avec le programme...
    while True:
        # Lui demander quoi faire.
        mode = input(
            """
            Que veux tu faire ?
            - Ecris 'ajouter' pour ajouter un nouveau mdp.
            - Ecris 'voir' pour voir l'ensemble de la base de données.
            - Appuis sur q pour quitter. 
            """).lower()
        
        # S'il veut quitter, on arrête le programme.
        if mode == "q":
            break
        
        if mode == "voir":
            view()
        elif mode == "ajouter":
            add()
        else:
            print("La réponse donnée n'est pas correcte.")
            continue