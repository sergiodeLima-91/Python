'''Faça um programa que leia um número inteiro e mostre a sua tabuada completa na tela.'''

print('=' * 21)
print('T  A  B  U  A  D  A')
print('=' * 21)
n = int(input('Deseja saber a tabuada de qual número?: '))
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))

'''Existe uma maneira de fazer a tabuada com o laço while.'''
