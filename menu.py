class menu(object):
    def showmenu():
        print("1 - Inscribir una persona en un taller")
        print("2 - Consultar inscripcion")
        print("3 - Consultar inscriptos")
        print("4 - Registrar pago")
        print("5 - Guardar inscripciones")
        print("0 - Salir")
        cond = False
        while not cond:
            op = int(input("Ingrese numero de opcion: "))
            if op in [1,2,3,4,5,0]:
                cond = True
        return op