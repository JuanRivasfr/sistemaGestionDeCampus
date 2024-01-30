import os
from .variables import save, getAll
def create():
    os.system('cls')
    print("""
++++++++++++++++++++++++++++++++++++++
+          Menu del camper           +
++++++++++++++++++++++++++++++++++++++
""")
    save({
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Edad" : int(input("Ingrese la edad del camper: "))
    })
    os.system('pause')

def read():
    print("""
++++++++++++++++++++++++++++++++++++++
+          Menu del camper           +
++++++++++++++++++++++++++++++++++++++
""")
    print(getAll())
    os.system('pause')

def update():
    nombre = input("Ingrese el nombre del camper: ")
    

def delete():
    print("El camper se elimino")

def menu():
    menuu = """
++++++++++++++++++++++++++++++++++++++
+          Menu del camper           +
++++++++++++++++++++++++++++++++++++++
"""
    menu = ["Guardar", "Buscar", "Actualizar", "Eliminar", "Salir"]
    while(True):
        os.system('cls')
        print(menuu)
        print("".join([f"{i+1}. {val}\n" for i, val in enumerate(menu)]))
        try:
            opc = int(input(":"))
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1: create()
                    case 2: read()
                    case 3: update()
                    case 4: delete()
                    case 5:
                        break
        except ValueError:
            print("La opcion no esta habilitada")


