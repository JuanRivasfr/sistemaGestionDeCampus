import os
#Lista campers
camper = list()
#Guarda los campers
def save():
    #Crea un array donde pide los datos
    inf = {
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Edad" : int(input("Ingrese la edad del camper: "))
    }
    #Guarda el diccionario dentro del array
    camper.append(inf)
    os.system('pause')

#Llama todos los registros de campers
def getAll():
    #For para llamar a todos los registro
    for i,value in enumerate(camper):
        print(f'ID: {(i+1)} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')
    os.system('pause')

#Llama un solo registro
def getOne(data):
    #Llama lo que esta adentro de un index y lo almacena en una variable
    value = camper[data]
    #Imprime el llamado
    print(f'ID: {data} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')

#Elimina un registro
def eliminate(index):
    #For para recorrer camper
    for i,value in enumerate(camper):
            #Comprara el index con el registro del usuario
            if index == i:
                os.system('cls')
                #Borra con pop y guarda el valor eliminado en value
                value = camper.pop(index)
                #Imprime el registro eliminado
                print(f'ID: {index+1} \nNombre: {value.get("Nombre")} \nApellido: {value.get("Apellido")} \nEdad: {value.get("Edad")} \n')
                print("El camper fue eliminado")
                os.system('pause')

#Actualiza un registro
def updat(value):
    #Pide los valores que quiere modificar
    inf = {
        "Nombre": input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Edad" : int(input("Ingrese la edad del camper: "))
    }
    #Lo ingresa en la posicion del array que desea
    camper[value] = inf
