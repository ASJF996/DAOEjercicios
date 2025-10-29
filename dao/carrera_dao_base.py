from abc import ABC,abstractmethod  
from modelos.Carrera import Carrera
from modelos.Estudiante import Estudiante
from modelos.Inscripcion import Inscripcion

class CarreraDaoBase(ABC):
    @abstractmethod
    def add_carrera(self,carrera:Carrera):...

    @abstractmethod
    def get_all_carreras(self)->list[Carrera]:...

class EstudianteDaoBase(ABC):
    @abstractmethod
    def add_estudiante(self,estudiante:Estudiante):...

    @abstractmethod
    def get_all_estudiantes(self)->list[Estudiante]:...

class InscripcionDaoBase(ABC):
    @abstractmethod
    def add_estudiante(self,inscripcion:Inscripcion):...

    @abstractmethod
    def get_all_estudiantes(self)->list[Inscripcion]:...