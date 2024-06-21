import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional

from pyhydroportail.core.HydroSerieStation import HydroSerieStation


class HydroProject:
    def __init__(self, path: Optional[Path] = None) -> None:
        self.path = None

        self.raw_series = []
        self.computed_series = []

    def appendSerie(self, serie: HydroSerieStation):
        self.raw_series.append(serie)

    def write(self):
        ET.Element("HydroProject")
