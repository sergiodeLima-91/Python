# Crie um programa que leia diversos números digitados pelo usuário e que fiquem armazanados numa lsta. Caso o número
# digitado pelo usuário já esteja na lista, ele não será adicionado. No final, o programa deve exibir todos os valores
# únicos digitados e em ordem crescente.

# SOLUÇÃO DADA POR GUANABARA:

numeros = list() # 1 - Criar a lista. Também é possível criar ela fazendo "numero = []"
while True: # 2 - Criar um laço 'enquanto' já que não sabemos o número exato de termos que iremos digitar.
                    # E colocamos o True para que haja inserção infinita de valores na lista.
    n = int(input('Digite um número: ')) # 3 - Entrada que cria efetivamente o laço 'enquanto' infinito.
    if n not in numeros: # 4 -Laço SE criado para caso o valor de entrada do usuário não estiver na lista.
        numeros.append(n) # Tradução: " Se o valor digitado pelo usuário e armazenado em 'n' NÃO estiver presente (in)
                          # na variável números, então acrescente este valor digitado na lista 'numeros'.
        print('Valor adicionado com sucesso.')
    else: # Caso contrário, mostre a mensagem abaixo.
        print('Valor duplicado! Não irei adicionar!')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn': # 5 - Criar um comando para que o programa pare caso o valor presente na variável 'r' seja 'n' ou 'M'.
        break
print('-=-' * 30)
numeros.sort() # 6 - Para colocar os valores em ordem crescente.
print(f'Você digitou os valores {numeros}')