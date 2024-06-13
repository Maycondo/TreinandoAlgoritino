class Conta:
    

    def __init__(self , numero , titular , saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    
    def extrato(self):
        print(f"Saldo: R${self.saldo}")
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor
 
# Instancia da Classe Conta

p1 = Conta(1232, "Nicolau", 2000)   
print(p1.titular)
p1.extrato() #Saldo: R$2000
p1.depositar(500)
p1.extrato() #Saldo: R$2500