# Para copiar uma lista é usado o processo de fatiamento de strings.

a = [1, 2, 3, 7]
b = a[:] # Significa que todos os valores da lista 'a' foram COPIADOS para a variável 'b'
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista b: {b}')