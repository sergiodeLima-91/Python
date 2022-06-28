# Escreva um prigrama que leia um valor em metros e o exiba convertido em quilômetros, hectômetros,
# decâmetros, decímetros, centímetros e milímetros.
from time import sleep
from random import choice
print('=' * 57)
print('C  O  N  V  E  R  S  O  R    D  E    M  E  D  I  D  A  S')
print('=' * 57)
n = float(input('Digite um número qualquer: '))
mensagens = ['Um momento por favor.','A computar...','One momment, please.']
random = choice(mensagens)
print(random)
sleep(2)
print(f'A medidade de {n} metros corresponde a: ')
print('{} quilômetros'.format(n / 1000))
print('{} hectômetros'.format(n / 100))
print('{} decâmetros'. format(n / 10))
print('{} decímetros'.format(n * 10))
print('{} centímetros'.format(n * 100))
print('{} milímetros'.format(n * 1000))