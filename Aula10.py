


class Conta:

    def __init__(self, name, surname, valor):
        self.name = name
        self.surname = surname
        self.valor = valor
        self.historico = []

            
    def extrator(self, ):
        print("")
        print("----EXTRATO DA CONTA----")
        historico = self.historico
        return f"Voce tem ${historico} reias"

    def depositar(self, valor):
        print("----DEPÓSITO NA CONTA----")
        Totalvalor = self.valor + valor
        self.historico.append(Totalvalor)
        return f"Depósito de R${valor} reais! "
    
    def sacar(self, valor):
        Totalvalor = valor - self.valor
        return f"O valor sacador da sua conta ${Totalvalor} reias! "
    
    def Conta_historico(self):
        print("Historico das transações: ")
        historico = self.historico
        return historico
    
"""class Corrente(Conta):

    def __init__(self, __agencia, conta, corrente):
        super().__init__(__agencia, conta, corrente)

    def depositar(self, valor):
        valorTotal = valor + valor
        return f"Depósito de R${valorTotal}"
"""

perso1 = Conta("Maycon", "Douglas", 2000)
#print(perso1.depositar(800))
#rint(perso1.extrator())
#print(perso1.sacar(400))
print(perso1.Conta_historico())