#Solicite ao usuário o valor de sua renda anual bruta e, em seguida,
#calcule e exiba o desconto do Imposto de Renda de acordo com a tabela progressiva de 2024.

#Faixa de Renda Anual Bruta                           Alíquota
 #Até R$ 56.072,00                                                0%
 #De R$ 56.072,01 a R$ 238.532,00                    7,50%
 #De R$ 238.532,01 a R$ 522.400,00                  15%
 #De R$ 522.400,01 a R$ 987.600,00                 22,50%
 #Acima de R$ 987.600,00                                   27,50%
while True:
    try:
        renda = float(input("digite sua renda mensal: "))

        if renda == 56.072:
            resultado = 0
        elif renda >= 56072.01 and renda <= 238.532:
            resultado = 7.50
        elif renda >= 238.532 and renda <= 522.400:
            resultado = 15
        elif renda >= 522.400 and renda <= 987.600:
            resultado = 22.50
        elif renda > 987.600:
            resultado = 27.50
        else:
             print(resultado)

    except ValueError:
         print("erro aq em screve direito seu animal")
    break
