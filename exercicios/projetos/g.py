# Solicite ao usuário um número de 1 a 12
# (representando um mês do ano) e exiba o nome correspondente ao mês (por exemplo, 1 para "Janeiro", 2 para "Fevereiro", etc.).

print("-=" * 40)
print("seja bem vindo")
print("-=" * 40)

mes = int(input("Digite um número de 1 a 12: "))
while True:
    try:
        if mes == 1:
            print("o mes é janeiro")
        elif mes == 2:
            print("o mes é fevereiro")
        elif mes == 3:
            print("o mes é março")
        elif mes == 4:
            print("o mes é abril")
        elif mes == 5:
            print("o mes é maio")
        elif mes == 6:
            print("o mes é junho")
        elif mes == 7:
            print("o mes é julho")
        elif mes == 8:
            print("o mes é agosto")
        elif mes == 9:
            print("o mes é setenbro")
        elif mes == 10:
            print("o mes é outubro")
        elif mes == 11:
            print("o mes é novenbro")
        elif mes == 12:
            print("o mes é dezenbro")
        else:
            print("kkk mo burro escreveu errado kkkkkkkkkkk . na proxima Digite um número entre 1 e 12.")
    except ValueError:(
    print("errado carai kkkk"))
    break

