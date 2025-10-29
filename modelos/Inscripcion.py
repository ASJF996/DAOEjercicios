class Inscripcion:
    def __init__(self, inscripcionid: int | None, Estudianteid: int, Carreraid: int,FechaInscripcion:str):
        self.inscripcionid =inscripcionid 
        self.Estudianteid = Estudianteid
        self.Carreraid = Carreraid
        self.FechaInscripcion = FechaInscripcion


    def __repr__(self) -> str:
        return f"Inscripcion ({self.inscripcionid}, '{self.Estudianteid}', '{self.Carreraid}','{self.FechaInscripcion}')"