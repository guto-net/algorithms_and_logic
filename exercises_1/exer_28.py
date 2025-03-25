import math

print("Medida em cm do raio do círculo")

try:
    R = int(input("Digite o raio (R): "))
except ValueError:
    print("Deve ser um número (int)")

area = 2 * math.pi * R

print(f"A media do raio em cm é {area:.2f} cm")