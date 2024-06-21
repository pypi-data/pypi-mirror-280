import re
from datetime import datetime
from pathlib import Path

from pyhydroportail.const import EXPORT_VARIABLES
from pyhydroportail.core.HydroSerieStation import HydroSerieStation
from pyhydroportail.utils import execute_requete

EXPORT_URL = "https://hydro.eaufrance.fr/stationhydro/ajax/{code}/series"


def parse_periode(raw_string):
    regex = r"^([0-9]{2}\/[0-9]{2}\/[0-9]{4})-([0-9]{2}\/[0-9]{2}\/[0-9]{4})$"
    match = re.match(regex, raw_string)
    if match:
        debut, fin = match.group(1), match.group(2)
    else:
        raise ValueError(f'Mauvais formatage de la période {raw_string}. Utiliser "dd/mm/aaaa-dd/mm/aaaa"')
    if datetime.strptime(debut, "%d/%m/%Y") > datetime.strptime(fin, "%d/%m/%Y"):
        raise ValueError(f"La date de début doit être antérieur à la date de fin ({raw_string}).")
    return debut, fin


def parse_reponse(reponse):
    value_factor = 1 if reponse["series"]["unit"] in ("m", "m3") else 0.001

    data = reponse["series"]["data"]
    times, values = [], []
    for record in data:
        times.append(datetime.strptime(record["t"], "%Y-%m-%dT%H:%M:%SZ"))
        values.append(record["v"] * value_factor)
    return times, values


def run_export(global_arguments, action_arguments):
    url = EXPORT_URL.format(code=action_arguments.code)

    exported_series = []
    grandeur = action_arguments.grandeur
    variable_type = EXPORT_VARIABLES[action_arguments.grandeur]["variable_type"]
    for periode in action_arguments.periodes:
        try:
            debut, fin = parse_periode(periode)
            payload = {
                "hydro_series[startAt]": debut,
                "hydro_series[endAt]": fin,
                "hydro_series[variableType]": variable_type[0],
                f"hydro_series[{variable_type[1]}]": grandeur,
                "hydro_series[statusData]": "most_valid",
            }
            if action_arguments.timestep is not None:
                payload["hydro_series[step]"] = action_arguments.timestep

            error, reponse = execute_requete(url, payload)
            if error:
                if "hydro_series[endAt]" in reponse.keys():
                    raise ValueError(reponse["hydro_series[endAt]"][0])
        except ValueError as error:
            raise ValueError(error)

        times, values = parse_reponse(reponse)

        serie = HydroSerieStation(
            f"{action_arguments.code}_{grandeur}_{periode.replace('-', '_').replace('/', '-')}",
            grandeur,
        )
        serie.setSerie(times, values)
        exported_series.append(serie)
        print(serie.getSerie())

    if not action_arguments.output_as_list and action_arguments.output_path:
        output_path = Path(action_arguments.output_path)
        output_path.mkdir(parents=True, exist_ok=True)
    for serie in exported_series:
        if action_arguments.output_as_list:
            print(serie.to_string())
        elif action_arguments.output_path:
            dest_file = output_path / f"{serie.name}.pyhydro.txt"
            serie.write_to_txt(dest_file)
