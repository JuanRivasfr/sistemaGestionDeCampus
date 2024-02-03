import modulos.camper as camper
import json


info = {
    "Nombre" : input("Ingrese el nombre: "),
    "Telefono" : [
        {
            f"{'Fijo' if(int(input('1. Fijo 0. Celular: '))) else 'Celular'}":
            input(f'Numero contacto {x+1}: ')
        }
        for x in range((int(input("Cuantos numeros de contactos tiene?: "))))
    ]
}
    

busqueda = input("Numero")
for x, val in enumerate(info["Telefono"]):
    if( busqueda in val.get("Celular")):
        print(val)