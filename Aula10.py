


class Conta:

    def __init__(self, name, surname, valor):
        self.name = name
        self.surname = surname
        self.valor = valor
        self.historico = []

            
    def extrator(self, ):
        print("")
        print("----EXTRATO DA CONTA----")
        return f"Voce tem ${self.historico} reias"

    def depositar(self, valor):
        self.Totalvalor = self.valor + valor
        historico = self.historico
        historico.append(f"Deposito de: ${valor} reais")
        return f"Depósito de R${valor} reais! "
    
    def sacar(self, valor):
        print("")
        self.Totalvalor = self.valor - valor
        self.historico.append(f"Foi feito um saque de ${valor} reais")
        return f"O valor sacador da sua conta ${valor} reias! "
    
    def Conta_historico(self):
        print('')
        print("----Historico da conta----")
        valor = self.valor
        historico = self.historico 
        print(f"Saldo anterio: ${valor} Reias")
        return historico, f"Saldo total: {self.valor} "
    
"""class Corrente(Conta):

    def __init__(self, __agencia, conta, corrente):
        super().__init__(__agencia, conta, corrente)

    def depositar(self, valor):
        valorTotal = valor + valor
        return f"Depósito de R${valorTotal}"
"""

perso1 = Conta("Maycon", "Douglas", 2000)
#print(perso1.depositar(1800))
#rint(perso1.extrator())
#print(perso1.sacar(400))
perso1.sacar(1000)
perso1.depositar(100)
print(perso1.Conta_historico())