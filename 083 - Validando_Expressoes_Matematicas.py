#Crie um programa no qual o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
#analisar se a expressão passada está com os parêntes abertos e fechados na ordem (e quantidade) correta.

expr = str(input('Digite a epxpressão: ')) #"expr" de expressão.
#Toda string é uma lista. Com o operador "for" é possivel pegar cada letra dessa string.
pilha = []
for simb in expr: #Expressão criada para analisar cada valor da string.
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Expressão inválida!')
# Neste elif existem duas possibilidades: Lista cheia ou lista vazia. Se a quantidade de valores de "pilha" for maior que
# zero (isto é, se ela não estiver vazia), então o último elemento de "pilha" será eliminado. Por que? Porque é uma expressão
# completá é composta por dois parênteses e não somente um.
#Porém, se "pilha" for igual a zero (isto é, estiver vazia) este ')' será inserido no final dela. No final das contas,a
# lógica diz respeito justamente ao fato de que NÃO DEVE TER ELEMENTOS NA LISTA "PILHA".
# Se o usuário colocar somente '(' como entrada, a expressão estará inválida, pois o valor da pilha não será zero, mas
# um. Se ele inserir ')', este caractere será inserido em "pilha", já que o IF que vem antes somente é aplicado se a
# quantidade de elementos presentes em "pilha" for igual a zero.
