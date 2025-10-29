class Estudiante:
    def __init__(self, estudianteid: int | None, nombre: str,apellido:str,fecha_nacimiento:str,genero:str,email:str ,telefono: str):
        self.estudianteid =estudianteid
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.email = email
        self.telefono = telefono

    def __repr__(self) -> str:
        return f"Estudiante({self.estudianteid}, '{self.nombre}', '{self.apellido}','{self.fecha_nacimiento}','{self.genero}','{self.email}','{self.telefono}')"