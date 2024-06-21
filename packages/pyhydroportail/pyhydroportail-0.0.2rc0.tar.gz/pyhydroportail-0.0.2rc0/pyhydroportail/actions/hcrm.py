from pathlib import Path

import pandas as pd

from pyhydroportail.core.HydroSerieStation import HydroSerieStation


def input_to_serie(input):
    name = input.name.replace(".pyhydro.txt", "")
    grandeur = name.split("_")[1]
    serie = HydroSerieStation(name, grandeur)
    serie.read_from_txt(input)
    return serie


def process_inputs(inputs):
    series = []
    for input in inputs:
        input = Path(input)
        if not Path(input).exists():
            raise ValueError(f"Le chemin d'entrée spécifié {input.as_posix()} n'existe pas.")

        if input.is_file() and str(input).endswith(".pyhydro.txt"):
            series.append(input_to_serie(input))
        elif input.is_dir():
            for x in input.iterdir():
                if x.is_file() and str(x).endswith(".pyhydro.txt"):
                    series.append(input_to_serie(x))

    if not all(serie.grandeur == series[0].grandeur for serie in series):
        raise ValueError("Les fichiers d'entrée ont des grandeurs différentes.")

    return series


def run_hcrm(global_arguments, action_arguments):
    if action_arguments.excel_name.endswith(".xlsx"):
        excel_name = action_arguments.excel_name
    else:
        excel_name = f"{action_arguments.excel_name}.xlsx"
    output_excel = Path(excel_name)
    if output_excel.exists():
        rep = input("Le fichier Excel existe.\nVoulez-vous l'écraser ? [O/n] ")
        if rep and rep.lower() not in ("o", "y"):
            print("Abandon")
            return

    series = process_inputs(action_arguments.inputs)
    grandeur = series[0].grandeur
    series_to_concat = []

    for serie in series:
        centered_reduced = serie.getCenteredReduced()
        centered_reduced["name"] = serie.name
        series_to_concat.append(centered_reduced)

    hcrm_serie = pd.concat(series_to_concat).pivot(columns="name", values=grandeur).interpolate()
    hcrm_serie.index.rename("Durée (j)", inplace=True)
    print(hcrm_serie)

    with pd.ExcelWriter(excel_name) as writer:
        hcrm_serie.to_excel(writer, sheet_name="hcrm")
