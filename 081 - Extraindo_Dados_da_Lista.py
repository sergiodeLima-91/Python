# Crie um programa que irá ler VÁRIOS NÚMEROS e armanenar eles numa lista e depois disso mostre:
# a) Quantos números foram digitados;
# b) A lista de valores, ordenada de forma decrescente;
# c) Se o valor 5 foi digitado e está ou não na lista.

print('=' * 67)
print('\033[34mE  X  T  R  A  I  N  D  O    D  A  D  O  S    D  A    L  I  S  T  A\033[m')
print('=' * 67)
lista = []
while True:
    n = int(input('Digite qualquer número: '))
    lista.append(n)
    p = (input('Deseja continuar? Pressione N para sair ou qualquer tecla para continuar: '))
    if p in 'Nn':
        break
lista.sort(reverse=True)
print('+=+' * 20)
if 5 in lista:
    print('Encontrei o valor 5 na lista!')
else:
    print('O valor 5 não foi digitado!')

print(f'Você digitou {len(lista)} número(s) no total.')
print(f'Os ítens na ordem inversa ficam assim: {lista}')

