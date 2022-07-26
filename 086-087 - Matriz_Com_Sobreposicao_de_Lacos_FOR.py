#086 - Faça um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre
# a matriz na tela com a formatação correta.

# 087 - Insira na matriz programas que:
# 1 - MOSTRE A SOMA DOS VALORES PARES DIGITADOS;
# 2 - A SOMA DOS VALORES DA TERCEIRA COLUNA;
# 3 - O MAIOR VALOR DA SEGUNDA LINHA.

# SOLUÇÃO DADA POR GUANABARA.

# Vamos criar a matriz com base numa lista com valores preenchidos com zero. Isso vai nos poupar o trabalho de ter que
# dar vários appends para preencher as listas de novo.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
scol = 0
mai = 0
# Necessário criação de laços um dentro do outro para o preenchimento de todas as linhas e colunas.
for l in range(0, 3): # Este é o "for" de alimentação, para colocar os valores dentro da matriz.
     for c in  range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
# Agora, precisamos colocar cada número numa estrutura de matriz 3x3:
for l in range(0, 3): # Já este "for" aqui servirá para mostrar, como já dito,a estrutura de matriz na tela.
    for c in  range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='') # A expressão "^5" centraliza os valores apresentados entre "[]". O número cinco é opcional.
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print() # Este print  (e o "=end''" na linha anterior) nessa posição é o segredo para deixar a matriz com três linhas e três colunas,
            # pois a cada repetição dos laços "for" aparecem três valores.
for l in range(0, 3):
    scol += matriz[l][2]
for c in range(0, 3):
    if  c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print(f'A soma dos números pares é {soma_par}')
print(f'A soma dos números da terceira coluna é {scol}.')
print(f'O maior valor da segunda linha é {mai}.')

# Todo o código foi construído por Guanabara :(