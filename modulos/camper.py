import os
from .variables import save, getAll, eliminate, camper
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
def read(codigo=None):
    print("""
++++++++++++++++++++++++++++++++++++++
+          Menu del camper           +
++++++++++++++++++++++++++++++++++++++
""")
    if(codigo==None):
        for i,value in enumerate(getAll()):
            print(f'ID: {(i+1)} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')
    else:
            value = getAll()[codigo-1]
            print(f'ID: {codigo} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')
    os.system('pause')
def update():
    nombre = input("Ingrese el nombre del camper: ")
def delete():
    os.system('cls')
    read()
    cd = int(input("Ingrese el codigo del camper que desea eliminar: "))
    read(cd)
    opc = int(input("Esta seguro que desea eliminar?\n1.Si \n2.No \n3.Salir \nIngrese el numero correspondiente: "))
    if opc == 1:
        for i,value in enumerate(getAll()):
            if cd-1 == i:
                os.system('cls')
                value = eliminate(i)
                print(f'ID: {cd} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')
                print("El camper fue eliminado")
                os.system('pause')
    elif opc == 2:
        delete()
    elif opc == 3:
        menu()
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
            os.system('pause')


