#ATIVIDADE 4 Solicite dois números e verifica qual deles é o maior e exiba uma mensagem correspondente.
print("-=" * 40)
print("seja bem vindo")
print("-=" * 40)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = 0

if num2 > maior:
  maior = num2
if num3 > maior:
  maior = num3

print(f"O maior número é {maior}")