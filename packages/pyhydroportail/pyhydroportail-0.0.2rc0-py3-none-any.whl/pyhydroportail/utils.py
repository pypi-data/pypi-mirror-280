from datetime import datetime

import requests


def execute_requete(base_url, payload):
    response = requests.get(base_url, params=payload)
    if response.status_code == 200:
        return False, response.json()
    elif response.status_code in (400, 500):
        return True, response.json()
    else:
        raise ConnectionError


def format_date(raw_date_string):
    if raw_date_string.endswith("Z"):
        parser = "%Y-%m-%dT%H:%M:%SZ"
    else:
        parser = "%Y-%m-%dT%H:%M:%S"
    return datetime.strptime(raw_date_string, parser).strftime("%d/%m/%Y")


def annee_service(debut, fin=""):
    date_debut = datetime.strptime(debut, "%d/%m/%Y")
    if fin:
        date_fin = datetime.strptime(fin, "%d/%m/%Y")
    else:
        date_fin = datetime.now()
    annee = int((date_fin - date_debut).days / 365.2425)
    return annee
