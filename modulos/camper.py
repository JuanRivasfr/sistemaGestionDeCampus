import os
from .variables import save, getAll, eliminate, camper, updat, getOne
#Funcion necesaria para crear registros
def create():
    os.system('cls')
    #Imprimo el menu
    print("""
++++++++++++++++++++++++++++++++++++++
+          Menu del camper           +
++++++++++++++++++++++++++++++++++++++
""")
    #Llamo al metodo encargado de guardar los campers
    save()
#Funcion necesaria para buscar los registros
    #Se le pone el (none) para crear una condicion de la funcion que busca
    #El parametro
def read(codigo=None):
    #Imprime el menu
    print("""
++++++++++++++++++++++++++++++++++++++
+          Menu del camper           +
++++++++++++++++++++++++++++++++++++++
""")
    #Si el parametro es vacio ejecutar
    if(codigo==None):
        #Llama el metodo para buscar todos los registros
        getAll()
    else:
        #Llama el metodo para buscar un registro solicitado por el usuario
        getOne(codigo)
#Funcion para editar 
def update():

    os.system('cls')
    #Llama a todos los registros para que el usuario los visualice
    read()
    #Le pide el codigo que desea ingresar
    cd = int(input("Ingrese el codigo del camper que desea editar: "))
    os.system('cls')
    #Llama el registro que el usuario piensa editar
    read(cd)
    #Menu de que hacer con el registro
    opc = int(input("Esta seguro que desea editar?\n1.Si \n2.No \n3.Salir \nIngrese el numero correspondiente: "))
    if opc == 1:
        os.system('cls')
        #Llama el metodo para editar y adicionalmente le resta uno debido a la logica de las posiciones de array
        updat(cd-1)
        os.system('cls')
        #Despues vuelve a mostrar el resgistro que ya fue editado
        read(cd)
        print("Se edito el camper")
        os.system('pause')
    elif opc == 2:
        #Se reinicia el metodo
        update()
    elif opc == 3:
        #Se devuelve al menu
        menu()
#Funcion para eliminar
def delete():
    os.system('cls')
    #Llama todos los registros a ser visualizados por el usuario
    read()
    #Le pide el codigo a ingresar
    cd = int(input("Ingrese el codigo del camper que desea eliminar: "))
    os.system('cls')
    #Llama el registro que el usuario quiere eliminar
    read(cd)
    opc = int(input("Esta seguro que desea eliminar?\n1.Si \n2.No \n3.Salir \nIngrese el numero correspondiente: "))
    if opc == 1:
        #Llama la funcion a eliminar y le resta uno al numero de acuerdo con la logica de los arrays
        eliminate(cd-1)
    elif opc == 2:
        #Reinicia el metodo
        delete()
    elif opc == 3:
        #Devuelve el menu
        menu()
def menu():
    menuu = """
++++++++++++++++++++++++++++++++++++++
+          Menu del camper           +
++++++++++++++++++++++++++++++++++++++
"""
    #Guarda las opciones en un array
    menu = ["Guardar", "Buscar", "Actualizar", "Eliminar", "Salir"]
    #While para ejecutar el menu
    while(True):
        os.system('cls')
        #Imprime el menu
        print(menuu)
        #Join para convertir lista a strings con separadores
        print("".join([f"{i+1}. {val}\n" for i, val in enumerate(menu)]))
        try:
            opc = int(input(":"))
            #Condicion para entrar al menu
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


