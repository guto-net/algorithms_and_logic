print("Calcula área em centimetros quadrados de um quadrado")

try:
    L = float(input("Medida em cm (L) do quadrado: "))
except ValueError:
    print("Deve ser um número (float)")


area = L ** 2

print(f"A área em cm quadrados é de {area:.2f}")