from manejadorTaller import manejadorT
from manejadorPersonas import manejadorP
from manejadorInscripciones import manejadorI
from menu import menu

if __name__ == '__main__':
    #manejadores
    mt = manejadorT()   #talleres
    mt.readtalleres()   #carga de talleres
    mp = manejadorP()   #personas
    mp.readarchivo()    #carga de personas (como base de datos de la propia escuela -> facilitar el ingreso de personas)
    mi = manejadorI()   #inscripciones

    band = False
    while not band:
        menu = menu()
        opcion = menu.showmenu()
        if opcion == 1:
            mt.regInsc(mp, mi)
        elif opcion == 2:
            mi.consulta_inscripcion()
        elif opcion == 3:
            mt.consulta_inscripto(mi, mp)
        elif opcion == 4:
            mi.regpago()
        elif opcion == 5:
            mp.savePersonas(mi)
        elif opcion == 0:
            print("Saliendo...")
            band = True
        else: print("Opcion incorrecta...")