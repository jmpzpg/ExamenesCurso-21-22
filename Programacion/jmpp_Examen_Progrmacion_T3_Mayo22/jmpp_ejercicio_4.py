'''
    Jose Manuel Perez Puig - 
    -1- Crear una base de datos SQLite con una tabla libros.
        libros(id, titulo, autor, genero, altura, editor)
    -2- Crear una función que lea los datos de los libros contenidos en el archivo libros.csv
        y los inserte en la tabla libros de la base de datos.
    -3- Obtener sendos resumenes de la BD. Uno por editorial y otro por autor
'''
import os
from clase_crud_sqlite import Sqlite
from clase_csv2Sqlite import Csv2TableSqlite

BASE_DATOS = 'libreria.db'
TABLA = 'libros'


def leer_datos_csv_a_tabla():
    '''
        Se crea la base de datos. Se crea la tabla y se llena con el contenido del csv.
    '''
    carga = Csv2TableSqlite('libros.csv', BASE_DATOS, TABLA)
    return carga.ejecutar()
    



def resumen_por_autor(filtro=None):
    '''
        Proporciona el conjunto de filas de la tabla agrupadas por autor con el numero de libros del mismo.
        Opcionalmente podemos filtrar esos resultados por el numero de libros. Debe ser un número > 0
    '''
    cadena = ''
    if filtro:
        cadena = f'(con más de {filtro} libros)'
        consulta_conteo = f'''select Autor, count(*) as num_libros 
                            from {TABLA}
                            group by Autor 
                            having num_libros > {filtro}
                            order by count(*) desc'''
    else:
        consulta_conteo = f'select Autor, count(*) as num_libros from {TABLA} group by Autor order by count(*) desc'
    print('')
    print(f'DATOS DE LA BIBLIOTECA: libros por autor ' + cadena)
    print('-------------------------------------------------------------------------')
    db = Sqlite(BASE_DATOS)
    return db.leer_tabla_condicion_cuenta(consulta_conteo)


def resumen_por_editorial(filtro=None):
    '''
        Proporciona el conjunto de filas de la tabla agrupadas por la editorial con el numero de libros de la misma.
        Opcionalmente podemos filtrar esos resultados por el numero de libros. Debe ser un número > 0
    '''
    cadena = ''
    if filtro:
        cadena = f'(con más de {filtro} libros)'
        consulta_conteo = f'''select Editor, count(*) as num_libros 
                            from {TABLA}
                            group by Editor 
                            having num_libros > {filtro}
                            order by count(*) desc'''
    else:
        consulta_conteo = f'select Editor, count(*) as num_libros from {TABLA} group by Editor order by count(*) desc'
    print('')
    print(f'DATOS DE LA BIBLIOTECA: libros por editorial ' + cadena)
    print('---------------------------------------------------------------------------')
    db = Sqlite(BASE_DATOS)
    return db.leer_tabla_condicion_cuenta(consulta_conteo)


def mostrar_resumen(resp):
    '''
        Muestra por pantalla los datos asociados al resumen pedido (resp)
    '''
    print('')
    for elem in resp:
        if elem[0] != '':
            print(f'{elem[0]}         {elem[1]}')


def main():
    '''
        Código de la aplicación principal
    '''
    os.system('clear')
    num = leer_datos_csv_a_tabla()
    print(f'Se cargaron {num} registros en la tabla {TABLA} de la base de datos {BASE_DATOS}')

    sigamos = True
    while sigamos:
        print('')
        print('¿Qué datos quiere revisar de nuestra biblioteca?\n')
        print('-1- Resumen de libros por Autor')
        print('-2- Resumen de libros por Editorial')
        print('')
        valor = input(f'Por favor, introduzca el número asociado a su selección: (Enter para salir)\n')
        if valor == '1':
            fil = input(f'Por favor, indique un numero mínimo de libros (>1, Enter para "todos"): ')
            if fil == '':
                filtro = 0
            else:
                filtro = int(fil)
            os.system('clear')
            resp = resumen_por_autor(filtro)
            mostrar_resumen(resp)
        elif valor == '2':
            fil = input(f'Por favor, indique un numero mínimo de libros (>1, Enter para "todos"): ')
            if fil == '':
                filtro = 0
            else:
                filtro = int(fil)
            os.system('clear')
            resp = resumen_por_editorial(filtro)
            mostrar_resumen(resp)
        elif valor == '':
            sigamos = False
            
        
        
            

# ==========================================
main()