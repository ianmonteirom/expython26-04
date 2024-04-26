"""
Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a. A média aritmética dos números armazenados na lista.
b. O somatório dos números pares armazenados na lista
"""

inteiros = []
soma_par = 0

for i in range(1, 10+1):
    n = int(input(f'Digite o {i}o número: '))
    inteiros.append(n)
    if n % 2 == 0:
        soma_par += n

media = sum(inteiros) / 10
print(f'Média aritmética dos valores digitados: {media:.2f}\n'
      f'Soma dos números pares: {soma_par}')
