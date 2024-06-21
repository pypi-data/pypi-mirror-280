from pyhydroportail.utils import annee_service, execute_requete, format_date

HUBEAU_URL = "https://hubeau.eaufrance.fr/api"
STATION_URL = f"{HUBEAU_URL}/v1/hydrometrie/referentiel/stations"
SITE_URL = f"{HUBEAU_URL}/v1/hydrometrie/referentiel/sites"

HUMAN_VALUES = {
    "influence_generale_site": {
        0: "Inconnue",
        1: "Nulle",
        2: "Etiage seulement",
        3: "Forte",
        4: "Hautes eaux seulement",
    },
    "influence_locale_station": {
        0: "Inconnue",
        1: "Nulle",
        2: "Etiage seulement",
        3: "Forte",
        4: "Hautes eaux seulement",
    },
    "statut_site": {
        1: "Avec signification hydrologique",
        2: "Sans signification hydrologique",
        3: "Source captée",
    },
}


def pretty_print_station(reponse):
    print(f"Station {reponse['code_station']} - {reponse['libelle_station']}")
    date_ouverture = format_date(reponse["date_ouverture_station"])
    msg = f"Ouverture le {date_ouverture}"
    if reponse["date_fermeture_station"] is not None:
        date_fermeture = format_date(reponse["date_fermeture_station"])
        msg += f" et fermeture le {date_fermeture} ({annee_service(date_ouverture, date_fermeture)} année(s))"
    else:
        msg += f" ({annee_service(date_ouverture)} année(s))"

    print(msg)
    if reponse["altitude_ref_alti_station"] is not None:
        msg = reponse["altitude_ref_alti_station"] / 1000
    else:
        msg = "-"
    print(f"Altitude de la station : {msg} m NGF")
    print(f"Influence locale : {HUMAN_VALUES['influence_locale_station'][reponse['influence_locale_station']]}")
    if reponse["commentaire_influence_locale_station"] is not None:
        print(f"Commentaire influence locale : {reponse['commentaire_influence_locale_station']}")
    print()
    if reponse["commentaire_station"] is not None:
        print(f"Commentaire station : {reponse['commentaire_station']}")


def pretty_print_site(reponse):
    print(f"Site {reponse['code_site']} - {reponse['libelle_site']}")
    print(f"Cours d'eau : {reponse['libelle_cours_eau']}")
    print(f"Superficie du bassin-versant : {reponse['surface_bv']} km²")
    print()
    print(f"Statut hydrologique : {HUMAN_VALUES['statut_site'][reponse['statut_site']]}")
    print(f"Influence générale : {HUMAN_VALUES['influence_generale_site'][reponse['influence_generale_site']]}")
    print()
    print(f"Commentaire sur le site : {reponse['commentaire_site']}")


def run_info(global_arguments, action_arguments):
    if len(action_arguments.code) == 8:
        url = SITE_URL
        payload_key = "code_site"
        pretty_print = pretty_print_site
    elif len(action_arguments.code) == 10:
        url = STATION_URL
        payload_key = "code_station"
        pretty_print = pretty_print_station
    else:
        raise ValueError(f"Le code indiqué ({action_arguments.code}) n'est pas un code de site ou station valide.")

    payload = {"format": "json", payload_key: action_arguments.code}
    _, reponse = execute_requete(url, payload)
    print()
    pretty_print(reponse["data"][0])
