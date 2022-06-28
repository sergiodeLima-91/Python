# Podemos inserir os valores da lista nos índices através de um imput. Aqui o script pede para inserirmos cinco números
# atraves de um input.

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores): # Aparentemente o 'c' está fazendo referencia a aos índices da lista e o 'v' aos valores inseridos neles.
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')