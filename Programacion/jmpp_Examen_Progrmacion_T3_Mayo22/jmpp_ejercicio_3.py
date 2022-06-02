'''
    Jose Manuel Perez Puig - Crear programa que crre un diccionario vacio y se vaya rellenando 
    el diccionario con información, sobre un vehículo, que se pide al usuario.
    Cada vez que se añade una pareja clave-valor se debe imprimir el diccionario.
'''
import os

os.system('clear')
diccionario = {}
sigamos = True
while sigamos:
    clave = input('¿Qué dato quiere introducir?\n')
    valor = input(f'Introduzca el valor para "{clave}":\n')
    diccionario[clave] = valor
    print(diccionario)
    resp = input('¿Quiere añadir más datos? (Si/No): ')
    if resp.lower() == 'no':
        sigamos = False
    
# =====================================