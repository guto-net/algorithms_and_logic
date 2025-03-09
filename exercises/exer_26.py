print("Medida do lado menor (m), lado maior (M), e do outro lado (O) do trapézio")

try:
    m = float(input("Digite o lado menor (m): "))
except ValueError:
    print("O lado menor (m) deve ser um número (float)")

try:
    M = float(input("Digite o lado maior (M): "))
except ValueError:
    print("O lado maior (M) deve ser um número (float)")

try:
    O = float(input("Digite o outro lado (O): "))
except ValueError:
    print("O outro lado (O) deve ser um número (float)")
    
perimeter = m + M + 2 * O

print(f"O perimetro do trapézio é de {perimeter} cm")