#ATIVIDADE 5  Solicite ao usuário um número de 1 a 7(representando um dia da semana) e exiba o nome correspondente ao dia (por exemplo, 1 para "Domingo", 2 para "Segunda-feira", etc.).6 - Solicite ao usuário três números inteiros e mostre o maior deles.7 - Solicite ao usuário um número de 1 a 12(representando um mês do ano) e exiba o nome correspondente ao mês (por exemplo, 1 para "Janeiro", 2 para "Fevereiro", etc.).8 - Solicite ao usuário o valor de sua renda anual bruta e, em seguida, calcule e exiba o desconto do Imposto de Renda de acordo com a tabela progressiva de 2024.Faixa de Renda Anual Bruta AlíquotaAté R$ 56.072,00 0%De R$ 56.072,01 a R$ 238.532,00 7,50%De R$ 238.532,01 a R$ 522.400,00 15%De R$ 522.400,01 a R$ 987.600,00 22,50%Acima de R$ 987.600,00 27,50%9 - Utiliza a biblioteca datetime para mostrar o ano, mes e dia da semana e pegar o horário atual e dar uma saudação para o usuário. Use o exemplo da imagem anexada

print("-=" * 40)
print("seja bem vindo")
print("-=" * 40)

dia = int(input("Digite um número de 1 a 7: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("inválido ou vc erro ou vc ta testando ne? . na proxima Digite um número de 1 a 7.")
