import os
camper = list()
def save():
    inf = {
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Edad" : int(input("Ingrese la edad del camper: "))
    }
    camper.append(inf)
    os.system('pause')

def getAll():
    for i,value in enumerate(camper):
        print(f'ID: {(i+1)} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')
    os.system('pause')

def getOne(data):
    value = camper[data]
    print(f'ID: {data} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')

def eliminate(index):
    for i,value in enumerate(camper):
            if index == i:
                os.system('cls')
                value = camper.pop(index)
                print(f'ID: {index+1} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')
                print("El camper fue eliminado")
                os.system('pause')

def updat(value):
    inf = {
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Edad" : int(input("Ingrese la edad del camper: "))
    }
    camper[value] = inf
