# Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares é
# possível ganhar.

d = float(input('Quanto te dinheiro há na carteira?  '))
conversao = d / 5.15
print('Com {} é possível comprar US$ {:.2f}'.format(d, conversao))