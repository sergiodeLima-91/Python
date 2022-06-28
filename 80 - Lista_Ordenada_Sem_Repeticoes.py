# Crie um prgrama onde  usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
# de inserção, sem usar o sort(). No final, mostre a lista ordenada na tela.

# SOLUÇÃO DADA POR GUANABARA:

# Precisamos criar um comando que coloque os valores digitados em ordem sem o comando sort(). Os números digitados pelo
# usuário podem estar nas seguintes posições: no início da lista (maior valor lido até agora), no meio dela, no final dela. Por isso não podemos inclusive
# usar o append, pois ele coloca valores somente NO FINAL da lista.

# 1 - CRIAR A LISTA
lista = []
# 2 - CRIAR O LAÇO DE REPETIÇÃO: Como nesse caso sabemos qual a quantidade de valores será digitada pelo
# usuário, usamos o FOR para criar um 'range'
for c in  range(0, 5):
# 3 - CRIANDO O COMANDO DE ENTRADA:
# Dentro do laço FOR, neste caso, não podemos usar o comando append, pois ele sempre colocará o número digitado pelo
# usuário no final da lista ou no início dela. Então usaremos um input normal dentro de uma variável
    n = int(input('Digite um valor: '))
# 4 - PRIMEIRO E O ÚLTIMO VALOR: Fazemos isso para mostrar que o primeiro valor sempre será o maior e o menos ao mesmo tempo.
    if  c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
# 5 - ORDENANDO OS NÚMEROS: É necessário descobrir as posições que os números devem ser posicionados. Para isso será
# necessário varrer todo o vetor.
    else:
        pos = 0 # "pos" de posição.
        while pos < len(lista): # Enquanto pos estiver na posição zero da lista...
            if n <= lista[pos]: # ...enquanto as posições de 'n' forem menores do que o número total de índices e valores
                                # da lista "lista"...
                lista.insert(pos, n) #...insira na "lista", na posição "pos", o valor 'n'.
                print(f'Adicionado na posição {pos} da lista.')
                break # Assim que 'pos' tiver um número maior do que a quantidade de índices de 'lista', o laço será parado.
            pos += 1 # Fazemos esse comando para que o 'pos' saia de zero e sempre receba um a mais.
print('-=' * 30)
print(f'Os valores digitados, em ordem, foram {lista}')