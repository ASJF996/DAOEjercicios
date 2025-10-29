import pyodbc
from modelos.Inscripcion import Inscripcion
from dao.carrera_dao_base import EstudianteDaoBase
from modelos.Estudiante import Estudiante  # Asegúrate de tener esta clase

class EstudianteDAOSQLserver(EstudianteDaoBase):
    def __init__(self, server, username, password, database):
        self.conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};UID={username};PWD={password};DATABASE={database}'
        )
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            IF NOT EXISTS (
                SELECT * FROM sysobjects WHERE name='Inscripcion' AND xtype='U'
            )
            CREATE TABLE Inscripcion (
                InscripcionID INT PRIMARY KEY IDENTITY(1,1),
                EstudianteID INT,
                CarreraID INT,
                FechaInscripcion DATE,
                FOREIGN KEY (EstudianteID) REFERENCES Estudiante(EstudianteID),
                FOREIGN KEY (CarreraID) REFERENCES Carrera(CarreraID)
            )
        """)
        self.conn.commit()

    def add_inscripcion(self, inscripcion: Inscripcion):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Inscripcion (EstudianteID, CarreraID, FechaInscripcion)
            VALUES (?, ?, ?)
        """, (
            inscripcion.Estudianteid,
            inscripcion.Carreraid,
            inscripcion.FechaInscripcion
        ))
        self.conn.commit()

    def get_all_inscripciones(self) -> list[Inscripcion]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT InscripcionId, EstudianteID, CarreraID, FechaInscripcion
            FROM Estudiante
        """)
        rows = cursor.fetchall()
        return [Estudiante(*row) for row in rows]