from classInscripcion import inscripcion
from classPersona import persona
from classTaller import TallerCapacitacion
from datetime import datetime
import numpy as np

class manejadorI:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento = 5):
        self.__ins = np.empty(dimension, dtype=inscripcion)
        self.__dimension = dimension
        self.__cantidad = 0
    
    def addInsc(self, i):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__ins.resize(self.dimension)
        self.__ins[self.__cantidad] = i
        self.__cantidad += 1

    def newinsc(self, fecha, tall, per):
        i = inscripcion(fecha, tall, per)
        self.addInsc(i)
        return i
    
    def ver_inscripto(self, dni):
        ins = None
        i = 0
        band = False
        while i < len(self.__ins) and band == False:
            p = self.__ins[i].getpersona()
            if p.getdni() == dni:
                ins = self.__ins[i]
                band = True
            else: i += 1
        return ins

    def consulta_inscripcion(self):
        dni = str(input("Ingresa el dni a consultar: "))
        ins = self.ver_inscripto(dni)   #verifica inscripto
        if ins != None:
            t = ins.gettaller()
            print('''
DNI: {}
Esta inscripta en {} y adeuda {}$
            '''.format(dni, t.getnombre(), t.getmonto()))

    def insc_taller(self, idT):
        for i in range(len(self.__ins)):
            t = self.__ins[i].gettaller()
            p = self.__ins[i].getpersona()
            if t.getid() == idT and p != None:
                print(p)

    def regpago(self):
        dni = int(input("Ingrese el dni de la persona: "))
        ins = self.ver_inscripto(dni)   #verifica inscripto
        if ins != None:
            ins.setpago()
            print("Pago registrado")
        else: print("({}) -> NO ESTA INSCRIPTA".format(dni))