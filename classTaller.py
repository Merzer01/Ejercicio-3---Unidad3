class TallerCapacitacion:
    __idTaller: int
    __nombre: str
    __vacantes: int
    __monto_inscripcion: int
    __inscripciones = []
    def __init__(self, idT, nomb, vac, monto):
        self.__idTaller = idT
        self.__nombre = nomb
        self.__vacantes = vac
        self.__monto_inscripcion = monto
        self.__inscripciones = []
    
    def __str__(self):
        return ('''
{} - {}
Precio: {}$
        '''.format(self.__idTaller, self.__nombre, self.__monto_inscripcion))
    
    def getid(self):
        return self.__idTaller
    def getnombre(self):
        return self.__nombre
    def getvacante(self):
        return self.__vacantes
    def getmonto(self):
        return self.__monto_inscripcion
    
    def addInscripcion(self, i):
        self.__inscripciones.append(i)

    def updatevac(self):
        self.__vacantes -= 1