"""
Faça uma função que recebe como parâmetro uma lista e um número. A função deve
retornar a quantidade de vezes que o número aparece na lista.
No programa principal, preencha a lista com 10 números aleatórios e solicite um número
ao usuário. Envie as informações para a função e exiba o seu retorno.
"""

from random import randint


def funcao(lista, num):
    quantidade = 0
    for i in range(len(lista)):
        if num == lista[i]:
            quantidade += 1
    return quantidade


aleatorio = []
for r in range(10):
    aleatorio.append(randint(1, 10))

n = int(input('Digite um número de 1 a 10: '))
print(f'Lista gerada de números aleatórios: {aleatorio}\n'
      f'O número {n} aparece {funcao(aleatorio, n)} vezes.')
