import pyodbc
from modelos.Estudiante import Estudiante
from dao.carrera_dao_base import EstudianteDaoBase

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
                SELECT * FROM sysobjects WHERE name='Estudiante' AND xtype='U'
            )
            CREATE TABLE Estudiante (
                EstudianteID INT PRIMARY KEY IDENTITY(1,1),
                Nombre NVARCHAR(100) NOT NULL,
                Apellido NVARCHAR(100) NOT NULL,
                FechaNacimiento DATE NULL,
                Genero CHAR(1) NULL,
                Email NVARCHAR(150) NULL,
                Telefono NVARCHAR(20) NULL
            )
        """)
        self.conn.commit()

    def add_estudiante(self, estudiante: Estudiante):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Estudiante (Nombre, Apellido, FechaNacimiento, Genero, Email, Telefono)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            estudiante.nombre,
            estudiante.apellido,
            estudiante.fecha_nacimiento,
            estudiante.genero,
            estudiante.email,
            estudiante.telefono
        ))
        self.conn.commit()

    def get_all_estudiantes(self) -> list[Estudiante]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT EstudianteID, Nombre, Apellido, FechaNacimiento, Genero, Email, Telefono
            FROM Estudiante
        """)
        rows = cursor.fetchall()
        return [Estudiante(*row) for row in rows]