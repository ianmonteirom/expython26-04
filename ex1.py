"""
Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista, e
os números ímpares em outra lista. Exiba as duas listas ao usuário.
"""

pares, impares = [], []
for i in range(1, 10+1):
    n = int(input(f'Digite o {i}o número: '))
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)

print(f'Lista de pares: {pares}\n'
      f'Lista de ímpares: {impares}')
