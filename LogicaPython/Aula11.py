
"""
Helloworld = ["H", "-", "e", "-", "l", "-", "l", "-", "o"]

for i in enumerate(Helloworld):
    if Helloworld == "-":
        continue
    print(i)

"""

name = input("Digite o seu nome: ")
numero  = int(input("Digite um número de 1 á 10: "))
email = input("Digite o seu email: ")

print("---" *10)
print("RESUTADOR ")
print("---" *10)
if len(name) >= 5:
  print("Seu nome tem mais de 5 letras")
else:
  print("Seu nome é curto!")

if numero <= 0:
  print("0 ou negativo não são permitidos.")
elif numero > 10:
  print("Numeros maior do que dez não permitidos")
else:
  print('Numero aceitavel!')

if "@" not in email or ".com" not in email:
  print ("E-mail inválido!")
else:
  print("E-mail válido.")