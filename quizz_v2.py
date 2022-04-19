print("Bienvenue pour ce petit quizz improvisé !")

playing = input("Acceptes-tu de répondre à 3 questions ? (O / n) ")

# S'il ne veut pas jouer, arrêter le programme.
if playing.lower() == "n":
    quit()

print("Okay ! C'est parti ! :)")
score = 0

def answer_is_correct(q: str, r: str) -> bool:
    """
    Fonction permettant de vérifier que la réponse donné par l'utilisateur est la bonne réponse à la question posée.

    Args:
        q:
        r:
    
    Return:
        True si la réponse est correcte sinon Faux.
    """
    answer = input(q)
    if answer.lower() == r:
        print('Correct!')
        return True
    else:
        print("Incorrect!")
        return False
    

score = score + 1 if answer_is_correct("Que veut dire le terme CPU ? ", "central processing unit") else 0
score = score + 1 if answer_is_correct("Que veut dire le terme GPU ? ", "graphics processing unit") else 0
score = score + 1 if answer_is_correct("Que veut dire le terme RAM ? ", "random access memory") else 0

print("Tu as répondu " + str(score) + " fois correctement.")
print("Tu as " + str((score / 3) * 100) + "% de réussite.")