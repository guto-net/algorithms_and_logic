age = int(input("Digite sua idade: "))

if age <= 12:
    print("Infantil")
elif 12 <= age <= 17:
    print("Adolescente")
elif 18 <= age <= 64:
    print("Adulto")
else:
    print("Idoso")