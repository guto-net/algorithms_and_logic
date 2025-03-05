'''
Entrada de dados em python
'''

salary: float; salary2: float
name: str; name2: str
age: int
gender: str

'''
Ele vai pegar o valor inserido na hora do input, e guardar na variável name
'''
name = input("Nome da primeira pessoa: ") 
salary = float(input("Salário da primeira pessoa: "))

name2 = input("Nome da segunda pessoa: ")
salary2 = float(input("Salário da segundo pessoa: "))

age = int(input("Digite uma idade: "))

gender = input("Digite um genêro: ")

print(f"Nome 1: {name}")
print(f"Salário 1: {salary:.3f}")

print(f"Nome 2: {name2}")
print(f"Salário 2: {salary2:.3f}")

print(f"Idade: {age}")

print(f"Genêro: {gender}")