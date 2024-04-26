"""
Preencha uma lista com 20 números inteiros aleatórios sorteados entre 1 e 50 e exiba:
a. a lista com todos os itens armazenados.
b. o somatório de todos os números contidos na lista.
c. o maior número da lista.
d. o menor número da lista.
"""

from random import randint

randoms = []
for r in range(20):
    n = randint(1, 50)
    randoms.append(n)

soma = sum(randoms)
print(f'Lista com todos os números aleatórios: {randoms}\n'
      f'Somatório de todos os números: {soma}\n'
      f'Maior número: {max(randoms)}\n'
      f'Menor número: {min(randoms)}')
