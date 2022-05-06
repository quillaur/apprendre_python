import random

# On compte le nombre de point pour le joueur et l'ordinateur.
user_wins = 0
computer_wins = 0

# On utilise un dictionaire pour les options possibles.
options = {
    "r": "rocher",
    "c": "ciseaux",
    "p": "papier"
}

# On fait une fonction pour demander à l'utilisateur le nombre de tours de la partie.
def ask_number(q: str, low: int, high: int) -> int:
    """
    The goal of this method is to ask a number from the user.
    The method needs to check that the user input is a number in the correct range before returning it.

    Args:
        q: the question to ask the user to input a number.
        low: the minimum number (inclusive) the user can give.
        high: the maximum number (inclusive) the user can give.
    
    Return:
        The int given by the user.
    """
    q_number = input(q)

    # Tant que ce n'est pas un chiffre, redemander un input à l'utilisateur.
    while not q_number.isdigit():
        print("Désolé, je n'ai pas reconnu le chiffre que tu m'as donné.")
        q_number = input(f"Entre un chiffre entre {low} et {high} stp. ")

    q_number = int(q_number)

    # Si le chiffre donné est insuffisant
    if q_number < low:
        print("Puisque tu ne veux pas jouer, on arrête là !")
        quit()

    # Si il est trop grand.
    elif q_number > high:
        print(f"Je n'ai pas autant de mémoire. J'en déduis donc que tu voulais dire {high}.")
        q_number = high
    
    return q_number

# On demande à l'utilisateur le nombre de tour.
turns = ask_number("Combien de tour veux-tu jouer ? (doit être un chiffre impair entre 1 et 10) ", 1, 10)
print("Tu veux faire une partie en", turns, "tours.")

# Pour tenter de ne pas avoir d'égalité, on vérifie que le nombre est impair.
while turns % 2 == 0:
    print("Ce chiffre n'est pas impair !")
    turns = ask_number("Entre un chiffre IMPAIR entre 1 et 10 stp: ", 1, 10)

# Définir les coups gagnants.
gagnant = [('r', 'c'), ('c', 'p'), ('p', 'r')]

# Tant que les joueurs sont execo.
while user_wins == computer_wins:
    # On boucle sur le nombre de tour.
    for i in range(turns):
        print("#####", "Tour", i, "#####")

        # On demande à l'utilisateur ce qu'il veut jouer ce tour-ci.
        user_input = input("Ecrit r (rocher) / c (ciseaux) / p (papier) ou q pour quitter: ").lower()
        if user_input == "q":
            print("Arrêt de la partie.")
            break
        
        # On vérifie que ce que l'utilisateur a entré correspond à nos attentes.
        if user_input not in options.keys():
            continue
        
        # L'ordinateur choisi son coup.
        computer_pick = random.choice(list(options.keys()))

        print("Tu as choisi:", options[user_input] + ".")
        print("L'ordinateur a choisi:", options[computer_pick] + ".")

        # On vérifi qui gagne.
        if (user_input, computer_pick) in gagnant:
            print("Tu as gagné !")
            user_wins += 1

        elif user_input == computer_pick:
            print("Egalité")

        else:
            print("Tu as perdu")
            computer_wins += 1

    print("Score:", user_wins, "/", computer_wins, "(you / computer)")

    # Si égalité, on relance pour 2 tours.
    if user_wins == computer_wins:
        print("Vous êtes à égalité ! Jouez 2 tours de plus pour vous départager !")
        turns = 2

print("Tu as gagné la partie !" if user_wins > computer_wins else "Tu as perdu !")