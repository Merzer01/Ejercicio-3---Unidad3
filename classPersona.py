class persona:
    __nombre: str
    __dni: int
    __direccion: str
    def __init__(self, nomb, doc, direc):
        self.__nombre = nomb
        self.__dni = doc
        self.__direccion = direc
    
    def __str__(self):
        return ("{} ({}) - Direccion: {}".format(self.__nombre, self.__dni, self.__direccion))
    
    def getdni(self):
        return self.__dni
    def getnombre(self):
        return self.__nombre