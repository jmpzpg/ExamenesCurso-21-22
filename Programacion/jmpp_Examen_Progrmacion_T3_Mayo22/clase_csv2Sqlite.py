import csv
from clase_crud_sqlite import Sqlite

def isfloat(num):
    '''
        Función auxiliar para determinar si una cadena puede ser un float
    '''
    try:
        float(num)
        return True
    except ValueError:
        return False



class Csv2TableSqlite():
    '''
        Clase que toma un archivo CSV, una BD y un nombre de tabla 
        y transfiere todos los datos del csv a la tabla de la BD,
        usando las cabeceras del csv como campos de la tabla.
    '''
    def __init__(self, csv_file, data_base, table_name) -> None:
        self.__csv_file = csv_file
        self.__db = data_base
        self.__table = table_name

    @property
    def db(self):
        return self.__db

    def ejecutar(self):
        self.__crear_tabla()
        return self.__llenar_tabla()


    def __crear_tabla(self):
        '''
            Crea la tabla en la base de datos.
        '''
        cadena_campos = self.__extraer_cad_campos_de_la_cabecera()
        db = Sqlite(self.__db)
        db.crear_tabla(self.__table, cadena_campos)
    

    def __llenar_tabla(self):
        db = Sqlite(self.__db)
        with open(self.__csv_file, 'r') as manejador:
            contenido = csv.reader(manejador)
            cabecera = next(contenido)
            num = db.insertar_muchos_registros(self.__table, cabecera, contenido)
        return num
    

    def __extraer_cad_campos_de_la_cabecera(self):
        '''
            Convierte la cabecera del csv en una cadena con la declaración de los campos de la tabla a crear.
            Devuelve una cadena con los campos y sus tipos. Precedida por el campo clave.
        '''
        with open(self.__csv_file, 'r') as manejador:
            contenido = csv.reader(manejador)
            cabecera = next(contenido)
            fila1_datos = next(contenido)
        return self.__extraer_tipos_datos_csv(cabecera,fila1_datos)


    def __extraer_tipos_datos_csv(self, cabecera, fila_datos):
        '''
            Extrae los tipos de datos del csv para poder declarar los campos de la tabla
        '''
        actual = 0
        cadena_campos = 'id integer primary key autoincrement,'
        for elem in fila_datos:
            cadena_campos += f'{cabecera[actual]} '
            if elem.isnumeric():        # es un numero en forma de cadena
                cadena_campos += f'int not null,'
            elif isfloat(elem):
                cadena_campos += f'decimal(7,4) not null,'
            else:
                cadena_campos += f'text not null,'
            actual += 1
        return cadena_campos[:-1]




# ======================================================



