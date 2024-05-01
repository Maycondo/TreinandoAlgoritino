# Relebrando Programaçao orienta a Objetos

class Perso:

    def  __init__(self, name, list_name):
        self.name = name
        self.list_name = list_name

    def Flando(self):
     aprensentado = "Olá prazer em conhecer voçê, meu nome é "
     return  f"{aprensentado}{self.name} {self.list_name}!"




p1 = Perso("Maycon", "Douglas")
print(p1.Flando())