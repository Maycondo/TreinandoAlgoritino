

name = input("Qual é o seu nome: ")
Yes_or_No = input(f"Hello , {name}! Você esta bem?? ")

if Yes_or_No.lower() == "Não" or Yes_or_No == "nao":
    print("Que pena! Espero que melhore...")
elif Yes_or_No.lower() ==  "Sim" or Yes_or_No == "sim":
    print("Que maravilha!")
else:
    print("Resposa invalida! Tente novamente.")

print("---"*10)
age = int(input("Qual e sua idade? "))


if age >= 18:
    print("Voce é maior de idade.")
elif  age >= 12 <= 15:
    print("Voce é adolecente")
elif age > 0 and age < 12 :
    print("Voce é uma criança")
else:
    print("Idade invalida!")


print("---" * 10)
ano_nascimento = 2024 - age
print(f"Você nasceu em {ano_nascimento}")


