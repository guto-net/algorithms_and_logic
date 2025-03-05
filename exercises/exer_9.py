user = str(input("Digite seu nome: "))

score = float(input("Digite seu ponto: "))

if score >= 7:
    print(f"O usuário {user} foi aprovado!")
elif 4 <= score <= 6.9:
    print(f"O usuário {user} está de recuperação!")
else:
    print(f"O usuário {user} foi reprovado!")