from modelos.Carrera import Carrera
from modelos.Estudiante import Estudiante
from dao.factory import get_dao_from_config
from dao.factoryestudiantes import get_daos_from_config


def menu():
    print("1-ingresar carrera")
    print("2-Mostrar carreras")
    print("0-Salir")
    return int(input('Digite la opcion que desee realizar'))
def menu2():
    print("1-ingresar estudiante")
    print("2-Mostrar Estudiantes")
    print("0-Salir")
    return int(input('Digite la opcion que desee realizar'))
def carreras():
    n=1
    
    while n!=0:
        dao= get_dao_from_config("config.json")
        n=menu()
        if n==1:
            
            carrera=input('Ingrese la carrera: ')
            facultad=input('A que facultad pertenece: ')
            dao.add_carrera(Carrera(None,carrera,facultad))
        elif n==2:
            for u in dao.get_all_carreras():
                print (u)

def estudiantes():
    n=1
    
    while n!=0:
        dao= get_daos_from_config("config.json")
        n=menu2()
        if n==1:
            
            nombre=input('Ingrese el nombre: ')
            apellido=input('Apellido: ')
            fecha_nacimiento=input('fecha de nacimiento: ')
            genero=input('genero: ')
            email=input('email: ')
            telefono=input('telefono: ')
            dao.add_estudiante(Estudiante(None,nombre,apellido,fecha_nacimiento,genero,email,telefono))
        elif n==2:
            for u in dao.get_all_estudiantes():
                print(u)

def main():
    
    #carreras()
    estudiantes()
if __name__ == "__main__":
    main()