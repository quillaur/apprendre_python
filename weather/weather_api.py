import requests

# On récupère la clef API stockée dans un fichier txt.
with open("weather/api_key.txt", "r") as f:
    API_KEY = f.read()

# On définit l'adresse en ligne qui nous permet de récupérer les données.
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Pour quelle ville ?
city = input("Pour quelle ville dois-je récupérer les données ? ")

# On construit la requête.
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric&lang=fr"

# On envoie la demande.
response = requests.get(request_url)

# Si on obtient une réponse valide (status_code = 200)
if response.status_code == 200:
    # On récupère le contenu de la réponse au format json.
    data = response.json()
    # Le json se manipule comme un dictionnaire en python.
    weather = " | ".join(elem['description'] for elem in data['weather'])
    temperature = data["main"]["temp"]

    print("Temps:", weather)
    print("Temperature:", temperature, "dégrées")
else:
    print("Une erreur c'est produite.")
