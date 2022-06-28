# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e menor
# valor digitado e as suas respectivas posições na lista.

mai = ''
men = ''
listanum = []
for c in range(0, 5): # Perceba 'cont' é uma variável e não precisou ser declarada anteriormente.
    listanum.append(int(input(f'Digite o valor da Posição 0{c}: ')))
    if c == 0: # Se C estiver na contagem 0, no primeiro índice, isto é, na primeira entrada do input no laço "if c cont in range"
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'A lista digitada foi {listanum}')
print(f'O maior número digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum): # Para enumerar (fazer uma varredura, uma análise) dos índices e valores na lista listanum.
    if v == mai: # Se v (de valor) for igual ao valor de 'mai', então printe na tela o índice formatado.
        print(f'{i}... ', end='') # 'end' Para que não haja quebra de linha.
print()
print(f'O menor número digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v ==men:
        print(f'{i}... ', end='')

#SOLUÇÃO DADA POR GUANABÁRA


