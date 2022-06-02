'''
    Jose Manuel Perez Puig - Crear funcion que reciba una lista de ceros y unos
    y devuelva su correspondencia en base 10
'''
import math

def binario2decimal(array):
    '''
        Función que recibe una lista de ceros y unos y devuelve su correspondencia en base 10
    '''
    exp = len(array)
    salida = 0
    for elem in array:
        exp -= 1
        salida += elem * (2 ** exp)    
    return salida


# ========================================

#print(binario2decimal([1,0,1,1,1,0,1]))
        