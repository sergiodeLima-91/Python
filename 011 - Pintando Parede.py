# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

A = float(input('Digite a altura de sua parede: '))
L = float(input('Digite a largura da parede: '))
print('Sua parede tem {} de altura por {} de largura.'.format(A, L))
print('São necessários {:.1f} litros de tinta para pintar toda a parede.'.format(A * L / 2 ))