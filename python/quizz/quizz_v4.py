import sys

# Mes questions:
q1 = "Combien de voiture(s) avez-vous ?"
q2 = "Avez-vous une assurance chez nous ? (oui/non)"
q3 = "Quel est votre adresse email ?"

# Stocker les réponses dans une variable.
reponses = []

# Poser les questions.
for i, q in enumerate([q1, q2, q3]):
    print(q)

    # Récupérer les réponses.
    for line in sys.stdin:
        # Enlever le /n de fin des strings.
        r = line.rstrip()

        # Vérifier le format des réponses.
        accepte = False
        if i == 0 and r.isdigit():
            reponses.append(r)
            accepte = True
        elif i == 1 and (r == "oui" or r == "non"):
            reponses.append(r)
            accepte = True
        elif i == 2 and "@" in r:
            reponses.append(r)
            accepte = True
        
        # Indiquer à l'utilisateur si tout va bien ou non.
        if accepte:
            print("Réponse acceptée.")
            break
        else:
            print("Votre réponse n'est pas acceptée. Veuillez saisir la bonne information.")
