# Crie um programa que leia o preço de um produto e mostre este mesmo preço com um desconto de
# cinco por cento.

v = float(input('Qual é o valor do produto?: '))
desconto = 5 / 100 * v
print('Valor do Produto: {:.2f}'.format(v))
print('Valor do desconto: {:.2f}'.format(desconto))
print('Novo valor com desconto: R$ {:.2f}.'.format(v - desconto))
