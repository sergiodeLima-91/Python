# Crie um algorítmo que leia nome e peso de várias pessoas, guarde as informações numa lista e no final mostre:
# 1 - Quantidade de pessoas cadastradas;
# 2 - Uma listagem com as pessoas mais pesadas;
# 3 - Uma listagem com as pessoas mais leves.

# SOLUÇÃO DADA POR GUANABARA:

temp = list() # Lista criada para armazenar os valores temporariamente.
princ = list() # Lista principal para armazenar os valores.
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0: # Se a quantidade de elementos de "princ" for igual a zero...
        mai = men = temp[1] # As variáveis MAI e MEN vão receber o valor presente no índice 1 da lista "temp", que é o peso.
    else:
        if temp[1] > mai: # É aquela velha jogada de Guanabara de assumir que o primeiro valor sempre será o maior e o menor
            mai = temp[1] # ao mesmo tempo, já que não tem nenhum valor digitado antes dele.
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:]) # Isso fara com que a lista "princ" receba uma cópia de todos os valores em "temp".
    temp.clear() # Para fazer com que não haja repetição de dados no print do terminal.
    resp = str(input('Quer continuar?[S/N]: '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.') # O uso do comando "len" pra mostrar a quantidade de valores em
# "princ" substitui a criação de uma variável "contador" pra mostrar o total de pessoas cadastradas pelo usuário.
print(f"O maior peso foi de {mai} Kg. Peso de ", end="")
for p in princ: # (PARA cada pessoa NA lista PRINC). Comando que faz uma varredura na lista, ainda que haja outra dentro dela.
    if p[1] == mai: # O que está entre as chaves é o índice da lista "princ" que tem o valor do peso. Se este valor
        print(f'[{p[0]}]', end='') # nesse índice for igual a MAI então print na tela o nome da pessoa que está no índice 0.
print()
print(f'O menor peso foi de {men} Kg. Peso de ', end="")
for p in princ: # A mesma lógica de cima se aplica aqui.
    if p[1] == men: # O recurso '=end' puxa para a linha de cima aquilo que está na linha de baixo.
        print(f'[{p[0]}]')
