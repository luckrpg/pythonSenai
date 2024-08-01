#ATIVIDADE 3 Solicite o ano de nascimento de uma pessoa, calcule a idade e verifica se a pessoa é maior ou menor de idade e exiba uma mensagem correspondente
print("-=" * 40)
print("seja bem vindo")
print("-=" * 40)
from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano_nascimento

if idade >= 18:
  print("Maior de idade.")
else
  print("Menor de idade.")

else
  print("invalido")