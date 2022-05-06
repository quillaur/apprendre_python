# La différence avec la v1 est qu'on veut jouer contre l'ordinateur maintenant.
# La difficulté est que toi, tu stock toutes les infos dans ton cerveau quand tu obtients un résultat.
# Avec l'ordi, il faut bien penser à tout stocker dans sa mémoire ! :)

import random

# L'ordinateur choisi un chiffre aléatoire entre 0 et 100.
random_number = random.randint(0, 100)

# Nombre de tentative pour que l'utilisateur trouve le chiffre.
guesses = 0

# Un booléen pour décider à qui c'est le tour de jouer.
my_turn = True # Honneur à l'humain.

# L'humain se rappel des coups joués.
# Pour permettre à l'ordinateur de faire pareil, nous stockerons les tentatives dans une liste.
all_values = list(range(101))
too_big = False

print("L'ordinateur a choisi un chiffre au hasard entre 0 et 100, peux-tu le deviner ?")
while True:

    # Si c'est à mon tour:
    if my_turn:
        # Incrémenter le nombre de tentatives.
        guesses += 1

        # Demander à l'utilisateur un chiffre.
        user_guess = input("Ta suggestion: ")

        # Vérifier que c'est bien un chiffre.
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print('Raté ! La prochaine fois entre un chiffre stp.')
            continue

    else:
        # L'ordinateur choisi la valeur en faisant une recherche dichotomique.
        # Explication de ce concept ici : https://www.codingame.com/learn/binary-search
        
        # On prend la valeur mediane de nos possibilités en trouvant l'index du milieu de la liste.
        half_index = len(all_values) // 2
        user_guess = all_values[half_index]
        print("L'orginateur choisi:", user_guess)
    
    # Vérifier que c'est bien le bon chiffre.
    if user_guess == random_number:
        print("Bien joué ! Le chiffre était ", user_guess, "!")
        break
    # Sinon, donner un indice à l'utilisateur.
    elif user_guess > random_number:
        print("Trop grand !")
        too_big = True
        # Conserver uniquement les valeurs en dessous du chiffre donné.
        if user_guess in all_values:
            all_values = all_values[:all_values.index(user_guess)]
    else:
        print("Trop petit !")
        too_big = False
        # Conserver uniquement les valeurs au dessus du chiffre donné.
        if user_guess in all_values:
            all_values = all_values[all_values.index(user_guess)+1:]
    
    # Donner le prochain tour à l'autre joueur.
    my_turn = not my_turn

if my_turn:
    print("Bien joué ! Tu as trouvé le bon chiffre en ", guesses, "coups et avant l'ordinateur !")
else:
    print("L'ordinateur gagne ! Il as trouvé le bon chiffre en", guesses, "coups et avant toi !")