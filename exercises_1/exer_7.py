age = int(input("Qual a sua idade? "))

if age < 16:
    print("Não pode votar!")
elif 16 <= age < 18:
    print("Voto opcional")
elif age >= 18:
    print("Voto obrigatório")