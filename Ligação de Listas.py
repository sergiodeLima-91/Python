# Qual a diferencça entre a ligação entre listas e cópia entre elas? Pode haver ligação entre elas desta maneira

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# Perceba que quando eu pedi para que houvesse  a substituição do 4 pelo 8 no comando 'b[2] = 8' no print mostra que as
# duas listas foram alteradas e não somente a lista 'a'. Isso porque elas estão LIGADAS pelo varíável 'b = a'