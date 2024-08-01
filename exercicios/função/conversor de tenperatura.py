def converter_temperatura(celsius):
  """Converte uma temperatura em graus Celsius para Fahrenheit e Kelvin.

  Args:
    celsius (float): A temperatura em graus Celsius.

  Returns:
    Uma tupla contendo a temperatura convertida para Fahrenheit e Kelvin.
  """

  fahrenheit = (celsius * 9/5) + 32
  kelvin = celsius + 273.15

  return fahrenheit, kelvin


# Exemplo de uso
temperatura_celsius = 25
fahrenheit, kelvin = converter_temperatura(temperatura_celsius)

print("Temperatura em Fahrenheit:", fahrenheit)
print("Temperatura em Kelvin:", kelvin)
