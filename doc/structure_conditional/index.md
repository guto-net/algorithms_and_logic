# Estrutura condicional

A estrutura condicional como já diz o nome e para uma condição, como é ter uma condição no código?

```python
hour = int(input("Digite uma hora do dia: "))

if hour < 12:
    print("Bom dia!")
elif hour < 18:
    print("Boa Tarde")
else:
    print("Boa Noite!")
```

Observe a forma que ela é estruturada, ultilizando if, elif(else if) e else...

if (se) hour >(operador maior) 12:
    print('Bom Tarde')

se a hora for maior do que 12 ele printa o Boa Tarde, simples e facíl a forma de usar uma condicional