num = [2, 3, 4, 4, 5, 6] #lista
num[0] = 10 # Comando para alterar o valor presente no índice (2, nesse caso) por 10.
num.append(8) # Comando para adicionar um índice no final da lista.
#num.sort(reverse=True) # Comando usado para colocar os valores dos índices em ordem decrescente. Caso eu queira
                       # deixar os números em ordem crescente, basta colocar o comando ".sort" sem o "reverse=True".
num.insert(2, 0) #Para inserir no índice 2 o valor  0. O valor que estava no índice selecionado é jogado para o indice
                 # seguinte em ordem crescente.
num.pop() # Vai excluir de forma automática o último valor da lista (6, no caso) junto com o índice. Para mais detalhes
          # sobre comandos de exclusão, vide caderno.
num.remove(10) # Comando que remove o valor presente no índice. Se voce colocar um valor que não está na lista, vai
               # dar erro. É possível colocar este comando dentro de um laço:
               # if 4 in num:
                    # num.remove(4)
                #else:
                    # print('Não achei o número quatro')
print(num)
print(f'Esta lista tem {len(num)} elementos.') #Mostra quantos índices a lista têm.




#DICA DE OURO ECONOMIZA MUITO TEMPO E LINHAS!!!!!

#print(*num, sep= ', ')# '*' mostra a lista sem os colchetes, e sep é a string entre as variáveis da lista
#input:[1, 2, 3]
#output: 1, 2, 3
