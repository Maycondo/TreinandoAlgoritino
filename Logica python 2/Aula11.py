import math




base = float(input("Digite numero da base do triangulo: "))
altura = float(input("Digite numero da altura do triangulo: "))


area = base * altura
perimitro = 2 * (base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimitro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")  #:.4f para