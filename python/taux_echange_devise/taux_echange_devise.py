import requests
import sqlite3
from datetime import datetime
import os

# API doc available at: https://www.exchangerate-api.com/docs/overview


def load_api_key(key_path: str) -> str:
    """
    On récupère la clef API stockée dans un fichier txt.

    Args:
        key_path: chemin vers le fichier contenant la clef API.
    
    Return:
        The API key.
    """
    if os.path.exists(key_path) and os.path.isfile(key_path):
        with open(key_path, "r") as f:
            api_key = f.read()
    else:
        raise Exception("ERROR: The filename either does not exists or is not a file !")
    
    return api_key


def create_request(currency: str, api_key: str) -> str:
    """
    Exemple de création de requête pour cette API: https://app.exchangerate-api.com/dashboard/confirmed
    On construit la requête.

    Args:
        currency: la devise qu'on veut échanger.
        api_key: la clef API
    
    Return:
        L'URL pour effectuer la requête API.
    """
    
    return f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}"


def get_currency_exchange_rate(currency: str, api_key: str) -> requests.Response:
    """
    Envoie de la requête API et récupération du résultat.

    Args:
        currency: la devise qu'on veut échanger.
        api_key: la clef API

    Return:
        Le contenu du résultat de la requête API.
    """
    url = create_request(currency, api_key)

    # On envoie la demande.
    response = requests.get(url)

    if response.status_code == 200:
        # On récupère le contenu de la réponse au format json.
        return response.json()
    else:
        # On gère les éventuelles erreurs.
        raise Exception(f"Error code {response.status_code} for URL: {response.url}")


if __name__ == "__main__":
    # Pour quelle devise ?
    given_currency = input("Pour quelle devise dois-je récupérer les données ? ").upper()

    # Vérfier que la devise est connue
    if not given_currency in ["USD", "EUR"]:
        print("Cette devise est inconnue !")
        quit()

    data_option = input("Souhaites-tu télécharger de nouvelles données ou voir celles déjà existantes ? (t/V")

    if data_option == "t":
        # On récupère les infos pour cet devise.
        api_key = load_api_key("taux_echange_devise/exchange_key.txt")
        data = get_currency_exchange_rate(given_currency, api_key)

        if data["result"] == "success":
            print("J'ai des données !")
        else:
            print("Je n'ai pas réussi à obtenir de données...")

        store_data = input("Souhaites-tu stocker ces données ? (O/n)")

        if store_data == "n":
            print("Ok, travail terminé.")
            quit()
        
        # Mettre le résultat en base de données (DB).
        # On se connecte à notre base de données. Si elle n'existe pas, elle sera automatiquement créée.
        con = sqlite3.connect("taux_echange_devise/currency.db")
        # On récupère un cursor qui nous permet d'effectuer des actions dans la DB.
        cur = con.cursor()

        # Pendant vos tests et débugs, vous pouvez être ammenés à créer / détruire vos tables plusieurs fois.
        # cur.execute("""DROP TABLE ExchangeRate""")

        # Création d'une table pour stocker nos données.
        cur.execute("""CREATE TABLE IF NOT EXISTS ExchangeRate 
                        (datetime, givenCurrency, demandedCurrency, rate)""")

        # Stockons juste les données qui nous intéressent.
        for demanded_currency in ["USD", "EUR", "CNY", "RUB", "GBP"]:
            if demanded_currency != given_currency:
                # Insertion des données en base.
                cur.execute(f"""INSERT INTO ExchangeRate 
                                VALUES ({data['time_last_update_unix']}, '{given_currency}', '{demanded_currency}', {data['conversion_rates'][demanded_currency]})""")

                # Sauvegarder le changement.
                con.commit()

        # Toujours penser à fermer la connection à la DB une fois les opérations faites.
        # Avant de fermer, assurez-vous toujours que les opérations ont été sauvegardées à l'aide de con.commit(), sinon elles seront perdues.
        con.close()

    else:
        # L'utilisateur souhaite voir les données dispo dans la DB pour la devise entrée.
        con = sqlite3.connect("taux_echange_devise/currency.db")
        cur = con.cursor()

        # On sélectionne les données relatives à la devise entrée par l'utilisateur et on boucle sur les résultats.
        for row in cur.execute(f"""SELECT * FROM ExchangeRate WHERE givenCurrency == '{given_currency}' ORDER BY datetime"""):
            # On convertit le timestamp en format lisible pour l'utilisateur.
            readable_date = datetime.utcfromtimestamp(row[0]).strftime("%Y-%m-%d %H:%M:%S")
            print(f"{readable_date}: {row[1]}/{row[2]} = {row[3]}")
