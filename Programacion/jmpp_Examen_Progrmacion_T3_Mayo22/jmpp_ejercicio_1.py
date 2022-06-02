'''
    Jose Manuel Perez Puig - Crear funcion que reciba cadena de texto y 
    devuelva la misma cadena con todas las palabras de mas de 4 letras invertidas
'''

def invierte_palabras_en_cadena(cadena):
    '''
        Invierte el orden,de los caracteres, de todas las palabras mayores de 4 caracteres
        de la cadena de entrada.
    '''
    lista_palabras = cadena.split(' ')
    salida = []
    for palabra in lista_palabras:
        if len(palabra) > 4:
            salida.append(palabra_al_reves(palabra))
        else:
            salida.append(palabra)
    return ' '.join(salida)


def palabra_al_reves(palabra):
    '''
        Toma la palabra de entrada e invierte el erden de todos sus caracteres.
    '''
    palabra_invertida = ''
    final = len(palabra)
    for i in range(final):
        final -= 1
        palabra_invertida += palabra[final]   
    return palabra_invertida


# ============================================

#cad = 'desde santurce a bilbao vengo por toda la orilla'
#print(cad)
#print(invierte_palabras_en_cadena(cad))