class coche:

    def __init__(self,marca,tipo): #Ojo doble barra baja en el init
        self.marca=marca
        self.tipo=tipo

    def dimeMarca(self):
        print("La marca del coche es "+self.marca)

    def tipoRueda(self):
        if self.tipo=="grande":
            print("Tu coche es 4x4")
        else:
            print("Tu coche no es 4x4")