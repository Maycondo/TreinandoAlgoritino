
"""
def Olamundo():

    Varievel = "Olá, Mundo!"
    return  Varievel


print(Olamundo())
"""
"""def soma(x , y):
    return x + y


print(soma(5,3))"""



def Ano_nacimento():

    Ano_nascimento = int(input("Digite o ano que vocẽ nasceu: "))
    Ano_atual = 2024

    idade_ano = Ano_atual - Ano_nascimento

    return(f"Sua idade é {idade_ano}")


def Hocimena():

    Hora_cimena = 20
    hora_atual = 2

    if hora_atual == Hora_cimena:
        print("Pode entrar!")
    elif hora_atual > Hora_cimena:
        print("A sessão ja acabou. Volte amanhã.")
    elif  hora_atual < Hora_cimena:
        print("A sessão ainda não começou")
    
    return hora_atual


print(Hocimena())