import time
from random import randint
print("")
print("")
print("seja bem vindo ao jogo de par ou inpar")
print("")
print("escolha 1 para jogar e 2 para sair")
escolha=True
while escolha:
    print("\n")
    print("\tJogo Par ou Impar")
    print("""
    1.Jogo
    2.Exit
    """)
    escolha= input("Digite a sua opção:   ")

    if escolha == "1":
        print('-=' * 40)
        print('\t\t\tVAMOS JOGAR PAR OU ÍMPAR')
        print('-=' * 40)
        opcao = ' '
        while opcao not in 'pi':
            opcao = str(input('Você quer par ou ímpar? (P/I) ')).lower().strip()[0]
        jogador = int(input('Digite um valor: '))
        pc = randint(0, 10)
        total = pc + jogador
        print(f'Você jogou {jogador} e o computador jogou {pc}. Total deu {total}.')
        print('Saiu PAR.' if total % 2 == 0 else 'Saiu ÍMPAR.')

        if opcao in 'p':
            if total % 2 == 0:
                print('Parabéns, ganhou o jogo.')
            else:
                print('Lamento, mas perdeu o jogo.')
        if opcao in 'i':
            if total % 2 == 1:
                print('Parabéns, ganhou o jogo.')
            else:
                print('Lamento, mas perdeu o jogo.')
        time.sleep(3)
    elif escolha == "2":
        print("Fim da Operação!")
        quit()
    else:
       print("\n Escolha não válida.\n Tente outra vez.")
