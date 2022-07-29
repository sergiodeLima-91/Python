# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte:
# 1) O valor da casa;
# 2) O salário do comprador e;
# 3) Em qunatos anos o empréstimo será pago.

#OBS: A prestação mensal não pode exceder 30% do salário do comprador!

'''valor =float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Em quantos anos pretende pagar? '))

prestacao = valor / (anos * 12)

if salario < 3000:
    print(f'NEGADO\nO valor do salário não atinge o limite mínimo de R$ 3000,00!')
elif prestacao > 30 * salario / 100:
    print('NEGADO')
    print(f'A prestação (R$ {prestacao:.2f}) excede o limite do valor (30%) que deve descontado de seu salário!')
elif anos > 30:
    print(f'NEGADO\nO tempo de quitação do empréstimo excede 30 anos!')
elif prestacao <= 30 * salario / 100:
    print(f'APROVADO\nSua prestação terá o valor de R$ {prestacao:.2f} mensais.')'''

print('-=-' * 23)
print('\033[1;31mA  P  R  O  V  A  Ç  Ã  O    D  E    E  M  P  R  É  S  T  I  M   O\033[m')
print('-=-' * 23)
casa = (float(input('Digite o valor da casa que deseja comprar: R$ ')))
salario =(float(input('Digite seu salário líquido: R$ ')))
tempo = int(input('Em quantos meses pretende pagar todo o valor?: '))
prestacao = casa / (tempo * 12)
if prestacao > 30 / 100 * salario:
    print('\033[1;31mNão é possível realizar o empréstimo!\nA parcela ultrapassa o limite de 30% de seu salário líquido!')
else:
    print('\033[1;32mEmpréstimo aprovado com sucesso!')