from pathlib import Path
from typing import Optional

import pandas as pd


class HydroSerieStation:
    def __init__(self, name: str, grandeur: str, times: Optional[list] = None, values: Optional[list] = None):
        self.name = name
        self.grandeur = grandeur
        self.serie = None

        if times is not None and values is not None:
            self.setSerie(times, values)

    def setSerie(self, times: list, values: list):
        self.times = times
        self.values = values

        data = {}
        data[self.grandeur] = self.values
        self.serie = pd.DataFrame(data=data, index=self.times)
        self.serie.index.rename("Date", inplace=True)

    def getSerie(self) -> pd.DataFrame:
        if self.serie is None:
            raise ValueError("Série non initialisée")
        return self.serie

    def getCenteredReduced(self):
        if self.serie is None:
            raise ValueError("Série non initialisée")

        centered_reduced = pd.DataFrame(self.serie[self.grandeur] / self.serie.max()[self.grandeur])
        centered_reduced.set_index(self.serie.index - self.serie.idxmax()[self.grandeur], inplace=True)
        return centered_reduced

    def to_string(self):
        return self.serie.to_string()

    def write_to_txt(self, filepath: Path, date_format: Optional[str] = "%d/%m/%Y %H:%M:%S") -> None:
        self.serie.to_csv(filepath, header=None, sep="\t", mode="w", date_format=date_format)

    def read_from_txt(self, filepath: Path, date_format: Optional[str] = "%d/%m/%Y %H:%M:%S") -> None:
        self.serie = pd.read_csv(
            filepath,
            header=None,
            sep="\t",
            names=["Date", self.grandeur],
            index_col="Date",
            date_format=date_format,
        )
