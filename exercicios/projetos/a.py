#ATIVIDADE 1 Solicite um número ao usuário e verifica se o número é positivo ou negativo e exiba uma mensagem positivo ou negativo.

print("-=" * 40)
print("seja bem vindo")
print("-=" * 40)
numero = float(input("Digite um número: "))
if numero > 0:
  print("O número é positivo.")
elif numero < 0:
  print("O número é negativo.")
else:
  print(f"invalido.")
