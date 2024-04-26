"""
Solicite os nomes e as idades de 10 pessoas. Armazene os nomes em uma lista e as
idades em outra lista.
Na sequência, exiba os nomes de todas as pessoas que possuem idade maior ou igual
a 18 anos.
"""

nomes, idades, maior_18 = [], [], []

for i in range(1, 10+1):
    nome = str(input(f'Digite o nome da {i}a pessoa: ')).strip().capitalize()
    nomes.append(nome)
    idade = int(input(f'Digite a idade da {i}a pessoa: '))
    print('--' * 24)
    idades.append(idade)
    if idade >= 18:
        maior_18.append(nome)

print(f'Pessoas maiores de 18 anos: {maior_18}')
