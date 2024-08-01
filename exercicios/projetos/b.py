#ATIVIDADE 2 Solicite duas notas de um aluno e calcule a média. Se a média for maior ou igual a 70, o aluno está aprovado. Caso contrário, está reprovado.
print("-=" * 40)
print("seja bem vindo")
print("-=" * 40)
nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 70:
    print("Aprovado!")
elif media >= 50 and media < 70:
    print("Reprovado kkk mo burro")
else:
    print("Reprovado")
