class Carrera:
    def __init__(self, carreraid: int | None, nombre: str, facultad: str):
        self.carreraid = carreraid
        self.nombre = nombre
        self.facultad = facultad

    def __repr__(self) -> str:
        return f"Carrera({self.carreraid}, '{self.nombre}', '{self.facultad}')"