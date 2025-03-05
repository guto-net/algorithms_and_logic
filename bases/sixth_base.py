'''
Estrutura condicional
'''

x = 10

print("Bom Dia")

if x < 8: # se x for menor do que 8, ele printa
    print("Boa Tarde")

print("Boa Noite")

hour = int(input("Digite uma hora do dia: "))

if hour < 12:
    print("Bom dia!")
elif hour < 18:
    print("Boa Tarde")
else:
    print("Boa Noite!")

