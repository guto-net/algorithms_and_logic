print("Conversão de graus Kelvin para Fahrenheit")

kelvin = float(input("Digite seu grau kelvin: "))

result = ((kelvin - 273.15) * 9 / 5) + 32

print("%.2f F" % (result))