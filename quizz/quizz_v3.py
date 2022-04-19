import random

print("Bienvenue pour ce petit quizz improvisé !")

playing = input("Acceptes-tu de répondre à quelques questions ? (O / n) ")

# S'il ne veut pas jouer, arrêter le programme.
if playing.lower() == "n":
    quit()

q_number = input("A combien de question(s) veux-tu répondres ? (max = 4) ")

# Tant que ce n'est pas un chiffre, redemander un input à l'utilisateur.
while not q_number.isdigit():
    print("Désolé, je n'ai pas reconnu le chiffre que tu m'as donné.")
    q_number = input("Entre un chiffre entre 1 et 4 stp. ")

q_number = int(q_number)

# Si le chiffre donné est insuffisant
if q_number < 1:
    print("Puisque tu ne veux pas jouer, on arrête là !")
    quit()

# Si il est trop grand.
elif q_number > 4:
    print("Je n'ai pas autant de questions en mémoire. Je ne t'en poserai donc que 4.")
    q_number = 4

print("Okay ! C'est parti ! :)")
score = 0

# Stock de questions / réponses.
q_a = {
    "Que veut dire le terme CPU ? ": "central processing unit",
    "Que veut dire le terme GPU ? ": "graphics processing unit",
    "Que veut dire le terme RAM ? ": "random access memory",
    "Que veut dire le terme PSU ? ": "power supply"
}

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
    
for i in range(q_number):
    # On selectionne une question aléatoire dans notre dictionnaire de questions.
    question = random.choice(list(q_a.keys()))

    score = score + 1 if answer_is_correct(question, q_a[question]) else 0

    # On retire cet élément du dictionnaire afin de ne pas retomber dessus aléatoirement.
    del q_a[question]

print("Tu as répondu " + str(score) + " fois correctement.")
print("Tu as " + str((score / q_number) * 100) + "% de réussite.")