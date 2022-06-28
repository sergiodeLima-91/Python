valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): # Aparentemente o 'c' está fazendo referencia a aos índices da lista e o 'v' aos valores inseridos neles.
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')