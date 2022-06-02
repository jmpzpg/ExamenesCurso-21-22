from OO.classPersona import Persona


def sumar(arg):
    total = 0
    if len(arg) == 0:
        return 0
    for val in arg:
        if type(val) is int or type(val) is float:
            total += val
        else:
            return 0
    return total

# ------------------------------------

def si_no_arg_devuelve_cero():
    return sumar([])
     
def si_lista_de_int_o_float_devuelve_suma():
    return sumar([1,3,5.5])
              
def si_cadenas_devuelve_cero():
    return sumar(['c', 3])

def si_num_complejos_devuelve_cero():
    return sumar([2+3j, 3])

def si_obj_no_numericos_devuelve_cero():
    p = Persona('Jose', 17, '12345678K')
    return sumar(p)

# ---------------------------------------


print(f'La respuesta de la prueba 1 es = {si_no_arg_devuelve_cero()}')
print(f'La respuesta de la prueba 2 es = {si_lista_de_int_o_float_devuelve_suma()}')
print(f'La respuesta de la prueba 3 es = {si_cadenas_devuelve_cero()}')
print(f'La respuesta de la prueba 4 es = {si_num_complejos_devuelve_cero()}')
#print(f'La respuesta de la prueba 5 es = {si_obj_no_numericos_devuelve_cero()}')