'''
    Clase que se ocupa del trabajo de conexión y gestión (CRUD) con la base de datos Sqlite.
    Parámetros:
        bd es la base de datos a la que nos queremos conectar y con la que trabajaremos.
        Se le pasa en el momento de instanciar la clase.
'''

import sqlite3

class Sql():
    '''
    Clase que se ocupa del trabajo de conexión y gestión (CRUD) con la base de datos Sqlite.
    Parámetros:
        bd es la base de datos a la que nos queremos conectar y con la que trabajaremos.
        Se le pasa en el momento de instanciar la clase.
    '''
    __cnx = None
    def __init__(self,bd) -> None:
        '''
            Constructor de la clase.
            Parámetros:
                bd - nombre (path) de la base de datos con la que trabajaremos
        '''
        self.__bd = bd
    
    def conectar(self):
        '''
            Crea nueva conexión con la BD.
            Devuelve la conexión.
        '''
        if self.__cnx is None:
            self.__cnx = sqlite3.connect(self.__bd)
        return self.__cnx

    def insert(self, articulo):
        '''
            Inserta una nueva fila en la tabla, que se extrae del tipo del parámetro de entrada
            Parámetro de entrada:
                objeto que modela un registro de una tabla de la BD. 
                Todos los datos están en el objeto.
            Devuelve el índice de la nueva fila de la tabla.
        '''
        cnx = self.conectar()
        cur= cnx.cursor()
        consulta = self.prepara_insert(articulo)
        cur.execute(consulta)
        new_id = cur.lastrowid
        cnx.commit()
        return new_id
    
    def select(self, consulta):
        '''
            Muestra los resultados de la consulta de selección dada.
            Parámetro de entrada:
                consulta a realizar
            Devuelve lista de tuplas con las filas seleccionadas.
        '''
        cnx = self.conectar()
        cur = cnx.cursor()
        cur.execute(consulta)
        filas = cur.fetchall()
        return filas

    def delete(self,articulo):
        '''
            Elimina un registro de la tabla dado el id.
            Parámetro de entrada:
                objeto que modela un registro de una tabla de la BD. 
                Todos los datos están en el objeto (la tabla y el id necesarios).
        '''
        tabla = type(articulo).__name__.lower()
        consulta = f'delete from {tabla} where id="{articulo.id}"'
        cnx = self.conectar()
        cur = cnx.cursor()
        cur.execute(consulta)
        cnx.commit()
    
    def update(self,articulo):
        '''
            Actualiza un registro de la tabla.
            Parámetro de entrada:
                objeto que modela un registro de una tabla de la BD. 
                Todos los datos están en el objeto.
        '''
        consulta = self.prepara_update(articulo)
        cnx = self.conectar()
        cur = cnx.cursor()
        cur.execute(consulta)
        cnx.commit()

    def prepara_insert(self,articulo):
        '''
            Método auxiliar para construir la consulta de inserción.
            Parámetro de entrada:
                objeto que modela un registro de una tabla de la BD. 
                Todos los datos están en el objeto (la tabla, los campos y los valores).
            Devuelve la consulta construida, lista para ser usada.
        '''
        tabla = type(articulo).__name__.lower()
        campos = tuple(vars(articulo).keys())
        datos = vars(articulo)
        valores = ''
        campos = ''
        for k,v in datos.items():
            if k != 'id':
                valores += f"'{str(v)}',"
                campos += f'{k},'
        consulta = f"insert into {tabla}({campos[:-1]}) values ({valores[:-1]});"
        return consulta
        
    def prepara_update(self,articulo):
        '''
            Método auxiliar para construir la consulta de actualización.
            Parámetro de entrada:
                objeto que modela un registro de una tabla de la BD. 
                Todos los datos están en el objeto (la tabla, los campos y valores y el id).
            Devuelve la consulta construida, lista para ser usada.
        '''
        tabla = type(articulo).__name__.lower()
        campos = vars(articulo)
        valores = ''
        for k,v in campos.items():
            if k != 'id':
                valores += f"{k}='{str(v)}',"
        consulta = f"update {tabla} set {valores[:-1]} where id = '{articulo.id}';"
        return consulta