from pyhydroportail.utils import execute_requete, format_date

SEARCH_URL = "https://hydro.eaufrance.fr/rechercher/ajax/entites-hydrometriques"
PAYLOAD = {
    "hydro_entities_search[label][value]": "",
    "hydro_entities_search[siteTypes][]": [
        "53b64673-5725-4967-9880-b775b65bdc9e",  # Site à débit moyen mensuel reconstitué (RECONSTITUE)
        "913a1b84-0e48-44e1-a7c7-ab8a867b34ee",  # Site plan d’eau (PLANDEAU)
        "e9bbe2dc-0f4c-4bed-88c0-bb9b984c5861",  # Site ponctuel (PONCTUEL) - Non activé par défaut
        "672aecb1-d629-426e-85a1-60882db8b30e",  # Site standard (STANDARD)
        "7a358b42-a4c6-4ee8-b019-722c1871cc3a",  # Site virtuel (VIRTUEL)
    ],
    "hydro_entities_search[active]": "1",
}


def pretty_print(sites_list):
    print(f"{len(sites_list)} site(s) trouvé(s).")
    for site in sites_list:
        if site != sites_list[-1]:
            tree1 = "├──"
            prefix1 = "│   "
        else:
            tree1 = "└──"
            prefix1 = "    "
        print(f"{tree1} {site['CdSiteHydro']} - {site['LbSiteHydro']}")

        if "stations" in site.keys():
            for station in site["stations"]:
                if station != site["stations"][-1]:
                    tree2 = f"{prefix1}├──"
                else:
                    tree2 = f"{prefix1}└──"
                prefix2 = f"{prefix1}    "
                print(f"{tree2} {station['CdStationHydro']} - {station['LbStationHydro']}")
                if "DtMiseServiceStationHydro" in station.keys():
                    date_mise_service = format_date(station["DtMiseServiceStationHydro"])
                    print(f"{prefix2} - Mise en service : {date_mise_service}")
                if "DtFermetureStationHydro" in station.keys():
                    date_fermeture = format_date(station["DtFermetureStationHydro"])
                    print(f"{prefix2} - Fermeture : {date_fermeture}")
        print(prefix1)


def run_search(global_arguments, action_arguments):
    if action_arguments.include_closed:
        PAYLOAD["hydro_entities_search[closed]"] = "1"

    PAYLOAD["hydro_entities_search[label][value]"] = " ".join(action_arguments.mot_clé)
    print(PAYLOAD)

    _, reponse = execute_requete(SEARCH_URL, PAYLOAD)
    pretty_print(reponse["sites"])
