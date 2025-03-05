# Saída de Dados em Python

No Python, podemos usar o operador `%` para formatar strings e exibir dados de forma personalizada. Aqui estão alguns exemplos comuns de formatação:

## Formatos Comuns

| Formato    | Descrição                                               | Exemplo de Uso                          |
|------------|---------------------------------------------------------|-----------------------------------------|
| `%s`       | Formata como **string**                                 | `"Meu nome é %s" % "João"` -> `Meu nome é João` |
| `%d`       | Formata como **inteiro decimal**                        | `"Idade: %d" % 25` -> `Idade: 25`      |
| `%.2f`     | Formata como **ponto flutuante** (float), limitando a 2 casas decimais | `"Valor de pi: %.2f" % 3.14159` -> `Valor de pi: 3.14` |
| `%5d`      | Formata como **inteiro**, reservando 5 espaços à esquerda | `"Número: %5d" % 42` -> `Número:   42`  |
| `%10s`     | Reserva **10 espaços** para a string, alinhando à direita | `"Nome: %10s" % "Maria"` -> `Nome:     Maria` |
| `%-10s`    | Reserva **10 espaços** para a string, alinhando à esquerda | `"Nome: %-10s" % "Maria"` -> `Nome: Maria     ` |

## Exemplos de Código

1. **Usando `%s` para formatar uma string**:

   ```python
   name = "João"
   print("Meu nome é %s" % name)
