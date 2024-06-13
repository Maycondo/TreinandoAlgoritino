from datetime import date



class Paciente:
    

    def __init__(self , name , idade , cpf , email):
        self.name = name
        self.idade = idade
        self.cpf = cpf
        self.email = email
    
    @classmethod
    def idadeAnoNascimento(cls , name , anoNascimento, cpf , email):
        idade = date.today().year - anoNascimento
        return Paciente(name , idade , cpf , email)

class Medico:
    pass







