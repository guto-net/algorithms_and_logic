number1 = int(input("Digite um numero: "))
number2 = int(input("Digite outro numero: "))

operator = str(input("Digite uma operador: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
else:
    print(number1 // number2)