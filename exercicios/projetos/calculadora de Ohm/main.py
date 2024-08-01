#Objetivo:Desenvolver uma Calculadora da Lei de Ohm automatizada para atender às
#necessidades da empresa. Essa ferramenta permitirá que os colaboradores:Calcule rapidamente e com precisão a resistência, a tensão ou a correnteelétrica.Calcule a resistência necessária para um resistor.Requisitos do Conversor:
#Funcionalidades:
#Cálculo da resistência, tensão e corrente em circuitos elétricos.
#Calcule a resistência necessária para um resistor.
#Simulação de diferentes cenários de conversão.
#Interface:Design amigável e profissional.Apresentação clara e organizada dos resultados.
#Segurança:Verificação contra entradas inválidas.


def calcular_resistencia(tensao, corrente):
    return tensao / corrente

def calcular_tensao(resistencia, corrente):
    return resistencia * corrente

def calcular_corrente(tensao, resistencia):
    return tensao / resistencia

def calcular_resistencia_necessaria(tensao, corrente_desejada):
    return tensao / corrente_desejada

def main():
    print("Bem-vindo à Calculadora da Lei de Ohm!")
    print("Selecione a operação que deseja realizar:")
    print("1. Calcular Resistência")
    print("2. Calcular Tensão")
    print("3. Calcular Corrente")
    print("4. Calcular Resistência Necessária para um Resistor")

    opcao = int(input("Digite o número da operação desejada: "))

    if opcao == 1:
        tensao = float(input("Digite a tensão (em volts): "))
        corrente = float(input("Digite a corrente (em ampères): "))
        resistencia = calcular_resistencia(tensao, corrente)
        print("A resistência é", resistencia, "ohms.")
    elif opcao == 2:
        resistencia = float(input("Digite a resistência (em ohms): "))
        corrente = float(input("Digite a corrente (em ampères): "))
        tensao = calcular_tensao(resistencia, corrente)
        print("A tensão é", tensao, "volts.")
    elif opcao == 3:
        tensao = float(input("Digite a tensão (em volts): "))
        resistencia = float(input("Digite a resistência (em ohms): "))
        corrente = calcular_corrente(tensao, resistencia)
        print("A corrente é", corrente, "ampères.")
    elif opcao == 4:
        tensao = float(input("Digite a tensão (em volts): "))
        corrente_desejada = float(input("Digite a corrente desejada (em ampères): "))
        resistencia_necessaria = calcular_resistencia_necessaria(tensao, corrente_desejada)
        print("A resistência necessária é", resistencia_necessaria, "ohms.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()