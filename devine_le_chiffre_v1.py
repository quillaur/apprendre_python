import random

# L'ordinateur choisi un chiffre aléatoire entre 0 et 100.
random_number = random.randint(0, 100)

# Nombre de tentative pour que l'utilisateur trouve le chiffre.
guesses = 0

print("L'ordinateur a choisi un chiffre au hasard entre 0 et 100, peux-tu le deviner ?")
while True:
    # Incrémenter le nombre de tentatives.
    guesses += 1

    # Demander à l'utilisateur un chiffre.
    user_guess = input("Ta suggestion: ")

    # Vérifier que c'est bien un chiffre.
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Essai encore, cette fois-ci en entrant un chiffre stp.')
        continue
    
    # Vérifier que c'est bien le bon chiffre.
    if user_guess == random_number:
        print("Bien joué ! Le chiffre était ", user_guess, "!")
        break
    # Sinon, donner un indice à l'utilisateur.
    elif user_guess > random_number:
        print("Trop grand !")
    else:
        print("Trop petit !")

print("Tu as trouvé le bon chiffre en ", guesses, "coups !")