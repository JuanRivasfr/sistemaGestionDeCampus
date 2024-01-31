import os
from .variables import save, getAll, eliminate, camper, updat
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
        os.system('pause')
    else:
            value = getAll()[codigo-1]
            print(f'ID: {codigo} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')   
def update():
    os.system('cls')
    read()
    cd = int(input("Ingrese el codigo del camper que desea editar: "))
    os.system('cls')
    read(cd)
    opc = int(input("Esta seguro que desea editar?\n1.Si \n2.No \n3.Salir \nIngrese el numero correspondiente: "))
    if opc == 1:
        os.system('cls')
        updat(cd-1)
        os.system('cls')
        read(cd)
        print("Se edito el camper")
        os.system('pause')
    elif opc == 2:
        delete()
    elif opc == 3:
        menu()
def delete():
    os.system('cls')
    read()
    cd = int(input("Ingrese el codigo del camper que desea eliminar: "))
    os.system('cls')
    read(cd)
    opc = int(input("Esta seguro que desea eliminar?\n1.Si \n2.No \n3.Salir \nIngrese el numero correspondiente: "))
    if opc == 1:
        eliminate(cd-1)
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


