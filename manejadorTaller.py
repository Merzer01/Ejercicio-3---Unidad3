from classTaller import TallerCapacitacion
from datetime import datetime
import csv
import numpy as np

class manejadorT:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento = 5):
        self.__talleres = np.empty(dimension, dtype=TallerCapacitacion)
        self.__dimension = dimension
        self.__cantidad = 0
    
    def addtaller(self, t):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__talleres.resize(self.__dimension)
        self.__talleres[self.__cantidad] = t
        self.__cantidad += 1
    
    def readtalleres(self):
        with open ('Talleres.csv', 'r', encoding='UTF-8') as archivo:
            lector = csv.reader(archivo, delimiter=';')
            next(lector)

            for row in lector:
                idT = row[0]        #id taller
                nomb = row[1]       #nombre
                vac = row[2]        #vacantes
                monto = row[3]     #precio
                t = TallerCapacitacion(idT, nomb, vac, monto)
                self.addtaller(t)

    def listado(self):
        for i in range(len(self.__talleres)):
            print(self.__talleres[i])

    def regInsc(self, mp, mi):
        self.listado()
        idT = int(input("Ingrese id del taller: "))
        tall = self.__talleres[idT-1]
        if tall.getvacantes > 0:
            per = mp.addPersona()
            fecha = datetime.now().date()
            insc = mi.newinsc(fecha, tall, per)
            tall.addInscripcion(insc)
            print("Ya estas inscripto!!!")
            tall.updatevac()
        else:
            print('''
El taller seleccionado no tiene lugares vacantes.
Ingrese otro taller de su interes
            ''')
            self.regInsc(mp, mi)

    def consulta_inscripto(self, mi):
        self.listado()
        idT = int(input("Ingrese id del taller a consultar: "))
        print("LISTADO DE INSCRIPTOS")
        mi.insc_taller(idT)
