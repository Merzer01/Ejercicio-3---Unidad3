from datetime import datetime

class inscripcion:
    __fecha: None
    __pago: bool
    __taller = None
    __persona = None
    def __init__(self, fecha, taller, persona, pago=False):
        self.__fecha = fecha
        self.__pago = pago
        self.__taller = taller  #instancia de la clase taller
        self.__persona = persona    #instancia de la clase persona

    def addPersona(self, p):
        self.__persona = p

    def setpago(self):
        self.__pago = True

    def getpersona(self):
        return self.__persona
    def gettaller(self):
        return self.__taller
    def getfecha(self):
        return self.__fecha