# Operadores

| Operador | Descrição                             | Exemplo             |
|----------|---------------------------------------|---------------------|
| `+`      | Adição                                | `3 + 2 = 5`         |
| `-`      | Subtração                             | `5 - 3 = 2`         |
| `*`      | Multiplicação                         | `4 * 2 = 8`         |
| `/`      | Divisão (resultado em float)         | `5 / 2 = 2.5`       |
| `//`     | Divisão inteira (arredonda para baixo) | `5 // 2 = 2`        |
| `%`      | Módulo (resto da divisão)            | `5 % 2 = 1`         |
| `**`     | Exponenciação                         | `2 ** 3 = 8`        |

## Operadores de Comparação
| Operador | Descrição                             | Exemplo             |
|----------|---------------------------------------|---------------------|
| `==`     | Igualdade                             | `3 == 3` (True)     |
| `!=`     | Diferença                             | `3 != 4` (True)     |
| `>`      | Maior que                             | `5 > 3` (True)      |
| `<`      | Menor que                             | `3 < 5` (True)      |
| `>=`     | Maior ou igual a                      | `5 >= 5` (True)     |
| `<=`     | Menor ou igual a                      | `3 <= 4` (True)     |

## Operadores Lógicos
| Operador | Descrição                             | Exemplo             |
|----------|---------------------------------------|---------------------|
| `and`    | Retorna `True` se ambas as condições forem `True` | `True and False` (False) |
| `or`     | Retorna `True` se pelo menos uma das condições for `True` | `True or False` (True) |
| `not`    | Retorna o oposto da condição          | `not True` (False)  |

## Operadores de Atribuição
| Operador | Descrição                             | Exemplo             |
|----------|---------------------------------------|---------------------|
| `=`      | Atribuição simples                    | `x = 5`             |
| `+=`     | Adição e atribuição                   | `x += 3` (equivalente a `x = x + 3`) |
| `-=`     | Subtração e atribuição                | `x -= 2` (equivalente a `x = x - 2`) |
| `*=`     | Multiplicação e atribuição            | `x *= 2` (equivalente a `x = x * 2`) |
| `/=`     | Divisão e atribuição                  | `x /= 2` (equivalente a `x = x / 2`) |
| `//=`    | Divisão inteira e atribuição          | `x //= 2` (equivalente a `x = x // 2`) |
| `%=`     | Módulo e atribuição                   | `x %= 3` (equivalente a `x = x % 3`) |
| `**=`    | Exponenciação e atribuição            | `x **= 2` (equivalente a `x = x ** 2`) |

## Operadores de Identidade
| Operador | Descrição                             | Exemplo             |
|----------|---------------------------------------|---------------------|
| `is`     | Verifica se duas variáveis referenciam o mesmo objeto | `x is y`            |
| `is not` | Verifica se duas variáveis não referenciam o mesmo objeto | `x is not y`        |

## Operadores de Membro
| Operador | Descrição                             | Exemplo             |
|----------|---------------------------------------|---------------------|
| `in`     | Verifica se um valor está contido em uma sequência (lista, tupla, etc.) | `5 in [1, 2, 3, 4, 5]` (True) |
| `not in` | Verifica se um valor não está contido em uma sequência | `7 not in [1, 2, 3, 4, 5]` (True) |

## Operadores Bitwise
| Operador | Descrição                             | Exemplo             |
|----------|---------------------------------------|---------------------|
| `&`      | E bit a bit                           | `5 & 3` (1)         |
| `|`      | OU bit a bit                          | `5 | 3` (7)         |
| `^`      | XOR bit a bit                         | `5 ^ 3` (6)         |
| `~`      | Negação bit a bit                     | `~5` (-6)           |
| `<<`     | Deslocamento à esquerda               | `5 << 1` (10)       |
| `>>`     | Deslocamento à direita                | `5 >> 1` (2)        |
