print("Bienvenue pour ce petit quizz improvisé !")

playing = input("Acceptes-tu de répondre à 3 questions ? (O / n) ")

if playing.lower() == "n":
    quit()

print("Okay ! C'est parti ! :)")
score = 0

answer = input("Que veut dire le terme CPU ? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Que veut dire le terme GPU ? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Que veut dire le terme RAM ? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Tu as répondu " + str(score) + " fois correctement.")
print("Tu as " + str((score / 3) * 100) + "% de réussite.")