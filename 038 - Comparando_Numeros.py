# Escreva um programa que leia dois números e diga qual deles é o maior ou que não há valor maior.

print('-=-' * 21)
print('\033[1;34mC  O  M  P  A  R  A  D  O  R     D  E     N  Ú  M  E  R  O  S\033[m')
print('-=-' * 21)
a = int(input('Digite o \033[1;031mprimeiro\033[m número: '))
b = int(input('Digite o \033[1;032msegundo\033[m número: '))
if a > b:
    print('O \033[1;31mprimeiro\033[m valor é maior!')
elif b > a:
    print('O \033[1;32msegundo\033[m valor é maior!')
else:
    print('Não existe valor maior, pois os dois são \033[1;35miguais!\033[m')