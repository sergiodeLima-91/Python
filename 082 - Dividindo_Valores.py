# Crie um programa que irá ler vários números e colocá-los em uma lista. Após isso, crie duas listas para conter os
# números ímpares e pares digitados pelo usuário.

print('-=-' * 20)
print('\033[34mV  A  L  O  R  E  S    E  M    C  A  D  A    L  I  S  T  A\033[m')
print('-=-' * 20)
print()
numero = []
numero_par = []
numero_impar = []
while True:
    n = int(input('Digite um número qualquer: '))
    numero.append(n)
    if n % 2 == 0:
        numero_par.append(n)
        print('INSERIDO NA LISTA DE NÚMEROS PARES!')
    else:
        numero_impar.append(n)
        print('INSERIDO NA LISTA DE NÚMEROS ÍMPARES!')
    p = (str(input('Continuar?: ')))
    if p in 'Nn':
        break
print('=' * 20)
numero.sort()
print(f'Você digitou o(s) total de {len(numero)} número(s) e ele(s) foi(ram) o(s) seguinte(s): {numero}')
print(f'O(s) número(s) par(es) foi(ram): {numero_par}')
print(f'O(s) número(s) ímpar(es) foi(ram): {numero_impar}')
