def create():
    print("El camper se guardo")

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
    print(menuu)
    menu = ["Guardar", "Buscar", "Actualizar", "Eliminar"]
    print("".join([f"{i+1}. {val}\n" for i, val in enumerate(menu)]))
    while(True):
        try:
            opc = int(input(":"))
            if(opc<=len(menu) and opc>0):
                print("")
                break
        except ValueError:
            print("La opcion no esta habilitada")


