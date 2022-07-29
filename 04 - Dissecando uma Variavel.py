#Faça um programa que leia algo pelo teclado  e mostre na tela o seu tipo primitivo e todas as informações
#possíveis sobre ele.
from  time import sleep
from random import choice
print('-=-' * 22)
print('\033[34mD  I  S  S  E  C  A  N  D  O    U  M  A    V  A  R  I  Á  V  E  L\033[m')
print('-=-' * 22)
print()
e = input('Digite um número inteiro qualquer: ') # Se eu não definir qual é o tipo primitivo da variável, o python estabele
 # que ela será do tipo string, independente do que seja inserido.
loading = ['Analisando...','Por favor, aguarde.','Mate kudasay' ]
escolha = choice(loading)
print(escolha)
sleep(3)
print('-' * 20)
print('\033[36mD I S S E C A Ç Ã O\033[m')
print('-' * 20)
print('> Tipo primitivo: '.format(e), type(e))
sleep(2)
if e.isspace():
    print('> Tem somente espaços.')
else:
    print('> NÃO tem somente espaços. ')
sleep(2)
if e.isnumeric():
    print('> É numérico.')
else:
    print('> NÃO é numérico.')
sleep(2)
if e.isalpha():
    print('> É alfabético.')
else:
    print('> NÃO é alfabético')
sleep(2)
if e.isalnum():
    print('> É alfanumérico.')
else:
    print('> NÃO é alfanumérico.')
sleep(2)
if e.isupper():
    print('> Está em maiúsculas.')
else:
    print('> NÃO está em maiúsculas.')
sleep(2)
if e.islower():
    print('> Está em minúsculas.')
else:
    print('> NÃO está em minúsculas.')
sleep(2)
if e.istitle():
    print('> Está capitalizada.')
else:
    print('> NÃO está capitalizada.')
print()
print('Obrigado por usar este programa! Deus te abençoe e te guarde!')