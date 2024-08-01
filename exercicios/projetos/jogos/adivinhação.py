import random

def jogar_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("")
    print("")
    print("tente adivinhar que numero eustou pensando")
    print("")
    print("")
    print("Estou pensando em um número entre 0 e 100...")
    numero_secreto = random.randint(0, 100)
    tentativas = 0

    while True:
        tentativa = int(input("Digite o seu palpite: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break

    jogar_novamente = input("Gostaria de jogar novamente? (sim/não): ")
    if jogar_novamente.lower() == "sim":
        jogar_adivinhacao()
    else:
        print("Obrigado por jogar!")

if __name__ == "__main__":
    jogar_adivinhacao()