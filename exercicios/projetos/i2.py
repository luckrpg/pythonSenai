import datetime

# Obter o horário atual
now = datetime.datetime.now()

# Extrair o ano, mês e dia da semana
ano = now.year
mes = now.month
dia_semana = now.strftime("%A")
dia = now.day

# Saudação
if now.hour < 12:
    saudacao = "Bom dia"
elif now.hour < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

# Exibir a saudação e as informações de data e hora
print(f"{saudacao}! Hoje é {dia_semana}, {dia} de {mes} de {ano}.")

