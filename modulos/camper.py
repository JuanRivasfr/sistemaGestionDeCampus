import os
def create():
    os.system('clear')
    print("""
++++++++++++++++++++++++++++++++++++++
+          Menu del camper           +
++++++++++++++++++++++++++++++++++++++
""")
    camper={
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Edad" : int(input("Ingrese la edad del camper: "))
    }
    print(camper)

def read():
    print("Datos del camper encontrados")

def update():
    print("El camper se actualizo")

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
        os.system('clear')
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


