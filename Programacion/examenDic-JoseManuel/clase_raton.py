class Raton():
    __posicion_x = 0
    __posicion_y = 0
    __boton_izquierdo = 0
    __boton_derecho = 0
   
    def get_posicion_x(self):
        return self.__posicion_x
    def get_posicion_y(self):
        return self.__posicion_y
    def get_boton_izquierdo(self):
        return self.__boton_izquierdo
    def get_boton_derecho(self):
        return self.__boton_derecho
    
# ----------------------------------------

    def set_posicion_x(self, px):
        self.__posicion_x = px
    def set_posicion_y(self, py):
        self.__posicion_y = py
    def set_boton_izquierdo(self, bi):
        self.__boton_izquierdo = bi
    def set_boton_derecho(self, bd):
        self.__boton_derecho = bd

# ----------------------------------------

    def click(self, boton):
        pass
    def doble_click(self, boton):
        pass
    def mover(self, px, py):
        pass
