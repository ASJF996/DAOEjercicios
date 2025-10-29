import pyodbc

from modelos.Carrera import Carrera
from dao.carrera_dao_base import CarreraDaoBase

class CarreraDAOSQLserver(CarreraDaoBase):
    def __init__(self,server,username,password,database):
        self.conn=pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};UID={username};PWD={password};DATABASE={database}'
        )
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            IF NOT EXISTS (
                SELECT * FROM sysobjects WHERE name='Carrera' AND xtype='U'
            )
            CREATE TABLE Carrera (
                CarrerID INT PRIMARY KEY IDENTITY(1,1),
                name NVARCHAR(100),
                Facultad NVARCHAR(100)
            )
        """)
        self.conn.commit()
    
    def add_carrera(self, carrera: Carrera):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Carrera (NombreCarrera,Facultad)
            VALUES (?, ?)
        """, (carrera.nombre, carrera.facultad))
        self.conn.commit()

    def get_all_carreras(self) -> list[Carrera]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT CarreraID, NombreCarrera, Facultad FROM Carrera")
        rows = cursor.fetchall()
        return [Carrera(*row) for row in rows]