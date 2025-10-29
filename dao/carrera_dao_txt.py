import os
from modelos.Carrera import Carrera
from dao.carrera_dao_base import CarreraDaoBase

class CarreraDAOTxt(CarreraDaoBase):
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("id,nombre,facultad\n")

    def add_carrera(self, carrera: Carrera):
        carrera_id = len(self.get_all_carreras()) + 1
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(f"{carrera_id},{carrera.nombre},{carrera.facultad}\n")

    def get_all_carreras(self) -> list[Carrera]:
        carreras = []
        with open(self.filepath, "r", encoding="utf-8") as f:
            next(f)  # Saltar encabezado
            for line in f:
                id_, nombre, facultad = line.strip().split(",")
                carreras.append(Carrera(int(id_), nombre, facultad))
        return carreras