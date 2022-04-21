import requests

# On récupère la clef API stockée dans un fichier txt.
with open("taux_echange_devise/exchange_key.txt", "r") as f:
    API_KEY = f.read()

# On définit l'adresse en ligne qui nous permet de récupérer les données.
BASE_URL = "https://v6.exchangerate-api.com/v6/"

# Pour quelle devise ?
given_currency = input("Pour quelle devise dois-je récupérer les données ? ").upper()

# Vérfier que la devise est connue

# On construit la requête.
request_url = f"{BASE_URL}{API_KEY}/latest/{given_currency}"

# On envoie la demande.
response = requests.get(request_url)

# Si on obtient une réponse valide (status_code = 200)
if response.status_code == 200:
    # On récupère le contenu de la réponse au format json.
    data = response.json()
    print(data)
else:
    print("Une erreur c'est produite.")