from classPersona import persona
import csv

class manejadorP:
    __lista = []
    def __init__(self):
        self.__lista = []
    
    def addPersona(self):
        print("Registro de datos personales")
        nomb = str(input("Ingrese nombre: "))
        dni = int(input("Ingrese documento: "))
        direc = str(input("Ingrese direccion: "))
        p = persona(nomb, dni, direc)
        return p
    
    def savePersonas(self, mi):
        enc = ['DNI','id Taller', 'Fecha de Inscripcion', 'Pago']
        with open ('PersonasInscriptas.csv', 'a+', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter=';')
            escritor.writerows(enc)
            for i in range(len(self.__lista)):
                dni = self.__lista[i].getdni()  #dni -> guardar
                ins = mi.ver_inscripto(dni)
                t = ins.gettaller()
                idT = t.getid() #id taller -> guardar
                fecha = ins.getfecha()  #fecha de inscripcion -> guardar
                pago_band = ins.getpago()
                if pago_band == True:
                    pago = 'Si' #pago (si) -> guardar
                else: pago = 'No'   #pago (no) -> guardar
                row = [dni, idT, fecha, pago]
                escritor.writerow(row)
        print("Se cargo el archivo PersonasInscriptas.csv de forma exitosa")