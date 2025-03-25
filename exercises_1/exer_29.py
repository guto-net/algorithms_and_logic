print("Calcula a área em cm quadrados de um triângulo")

try:
    B = float(input("Medida da base em cm (B): "))
except ValueError:
    print("Deve ser um número (float)")

try:
    A = float(input("Altura (A): "))
except ValueError:
    print("Deve ser um número (A)")

area = (B * A) / 2

print(f"A área em centimetros quadrados é de {area:.2f}")