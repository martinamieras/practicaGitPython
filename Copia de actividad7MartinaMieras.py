class Mamifero():
    def __init__(self,esperanzaDeVida, cantMamas):
        self.esperanzaDeVida= esperanzaDeVida
        self.cantMamas= cantMamas
    
    def mamar (self):
        print("da de mamar")
    def __nacer__(self):
        print("esta naciendo")

class AnimalMarino():
   def __init__(self,tieneBranqueas, especie):
       self.tieneBranqueas= tieneBranqueas
       self.especie= especie
    
   def __nadar__(self):
        print("el animal nada")

class Cetaceo(Mamifero,AnimalMarino):
    def __init__(self, esperanzaDeVida, cantMamas,tieneBranqueas, especie, notas, viveEn, peso):
        Mamifero.__init__(self,esperanzaDeVida, cantMamas)
        AnimalMarino.__init__(self,tieneBranqueas,especie)
        self.notas=notas
        self.viveEn=viveEn
        self.peso=peso
    def __nacer__(self):
       print("nace el cetaceo")
    def __nadar__(self):
       print("nada el cetaceo")

cetaceo1 = Cetaceo(1,"si","pez","vive debajo del mar","playa del carmen", 0,100)
cetaceo1.__nadar__()