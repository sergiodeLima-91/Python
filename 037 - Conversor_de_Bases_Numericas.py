# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.

# SOLUÇÃO DADA POR GUANABARA

num = int(input('Digite qualquer número inteiro: '))
print('[1] PARA BINÁRIO')
print('[2] PARA OCTAL')
print('[3] PARA HEXADECIMAL')
opcao = int(input(f'Para qual formato deseja converter o número  {num}? \n[1][2][3]: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.') # Este "[2:]" irá retirar do print os símbolos das numerações e deixar somente os
elif opcao == 2:                                                      # números correspondetes a conversão  de "num" pelo sistema escolhido.
    print(f'{num} conertido para OCTAL é igual a {oct(num)[2:]}.')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]} ')
else:
    print('Opção inválida! Tente novamente!')

# INFORMAÇÃO ÚTIL:
# O python exibe, respectivamente, cada um dos símbolos abaixo para representar os sistemas de numeração:
# "0x" - PARA HEXADECIMAL
# "0o" - PARA OCTAL
# '0b" - PARA BINÁRIO

# Para retirar esses símbolos do print basta fazer um comando de FATIAMENTO DE STRINGS: "[2:]" Pronto! Só aparecerá
# o número desejado.

