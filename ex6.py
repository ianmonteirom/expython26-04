"""
Solicite uma quantidade indeterminada de notas de alunos (até que seja informada uma
nota menor que zero). Após a entrada de dados, exiba:
a. A quantidade de notas que foram informadas.
b. Todas as notas na ordem em que foram informadas.
c. A média aritmética de todas as notas.
d. A quantidade de notas acima da média aritmética calculada.
"""

notas = []
cont = 1

while True:
    nota = float(input(f'Digite a {cont}a nota: '))
    print('--' * 24)
    if nota < 0:
        break
    notas.append(nota)
    cont += 1

cont -= 1
media = sum(notas) / cont
qnt_acima = 0

for a in range(len(notas)):
    if notas[a] > media:
        qnt_acima += 1

print(f'Quantidade de notas informadas: {cont}\n'
      f'Todas as notas em ordem: {notas}\n'
      f'Média aritmética de todas as notas: {media:.2f}\n'
      f'Quantidade de notas acima da média: {qnt_acima}')
