print("Perímetro em cm de um polígno regular")

try:
    Q = int(input("Digite a quantidade de lados do poligno (Q): "))
except ValueError:
        print("O valor deve ser um número (int)")

try:
    cm = float(input("Digite a medida em cm: "))
except ValueError:
     print("O valor deve ser um número (float)")

perimeter = Q * cm

print(f"O perimetro do poligno é {perimeter} cm")
