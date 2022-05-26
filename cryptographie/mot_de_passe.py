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


def view_credentials(fernet: Fernet) -> None:
    """
    Méthode pour voir les identifiants / mots de passes stockés dans passwords.txt.
    """
    print("Identifiants / MDP stockés:")
    if exists("password.txt"):
        with open("password.txt", "rb") as f:
            for line in f.readlines():
                credentials = fernet.decrypt(line)

                id, mdp = credentials.decode("utf-8").split(" | ")
                print(f"""
                        Identifiant: {id}
                        MDP: {mdp}
                        """)
    else:
        print("WARNING ! : aucun mots de passe sauvegardés jusqu'à présent.")


def store_credentials(id: str, password: str, fernet: Fernet) -> None:
    """
    Méthode pour écrires les identifiants / mots de passes dans passwords.txt.
    """
    credentials = f"{id} | {password}"
    token = fernet.encrypt(credentials.encode())

    with open("password.txt", "a") as f:
        f.write(token.decode("utf-8") + "\n")
    
    print(credentials, "stocké.")


if __name__ == '__main__':

    # Si nous n'avons jamais créé la clef,
    # alors il faut la générer et la sauvegarder dans un fichier.
    if not os.path.exists("key.key"):
        write_key()
    else:
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
            view_credentials(fer)

        elif mode == "ajouter":
            id = input("Entrer l'identifiant à stoker: ")
            mdp = input("Entrer le mot de passe à stocker: ")
            store_credentials(id, mdp, fer)
            
        else:
            print("La réponse donnée n'est pas correcte.")
            continue