# Crie um programa no qual o usuário possao digitar sete valores numéricos e cadastre-os em uma lista única que
# matenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# >>> EXIGÊNCIA: DEVE HAVER APENAS UMA LISTA QUE TEM DENTRO DELA MAIS DUAS.

princ = list()
par = list()
impar = list()

for c in range(1, 8):
    n = int(input(f'Digite o {c}° número:  '))
    if n %2 == 0:
       par.append(n)
    else:
        impar.append(n)
princ.append(par[:])
princ.append(impar[:])
print('-=' * 25)
princ[0].sort()
princ[1].sort()
print(f'Os números pares foram {princ[0]}')
print(f'Os números ímpares foram {princ[1]}')