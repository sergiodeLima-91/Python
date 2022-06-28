# Este programa destina-se a estudantes que desejam revisar determinado (s) assunto (s) estudado (s)
# através de perguntas e respostas.

from random import choice
print('=' * 34)
print('R  E  V  I  S  A  L  L    R  X  W')
print('=' * 34)
p_1_1 = ('1) É uma linguagem de programação')
p_1_2 = ('2) É uma linguagem de modelagem das funções de um sistema')
p_1_3 = ('3) Significa Sistema de Modelagem Unificado')
lista_de_escolha_1 = [p_1_1, p_1_2, p_1_3]
print('PERGUNTA 01 - O que é UML?')
random = choice(lista_de_escolha_1)
print()
p_1 = int(input('Digite o número correspondente a sua resposta: '))
print('')
print('''PERGUNTA 02 - Para que serve a UML?
1) Para programar um sistema com base em seus principais elementos, isto é, classes, atributos e métodos.
2) Para programar um sistema de forma a não implementar, inicialmente, as funcionalidades e não detalhar as mesmas.
3) Serve para modelar um sistema com base em seus ´principais elementos de composição, isto é, classes, atributos e métodos.''')
p_2 = int(input('Digite o número correspondente a sua resposta: '))
print('')
print('''PERGUNTA 03 - Assinale a alternativa que apresenta a correta definição do que é classe, atributo e método, respectivamente:
1) Classe pode ser definida como um ítem físico no mundo real; os atributos são as características da classe e; os métodos são as funções ligadas à classe.
2) Classe pode ser definida como um ítem, físico ou abastrato, presente no mundo real; os atributos são as características dessa classe e; os métodos são
   as funções que tal classe irá executar no sistema.
3) As classes nada mais são do que os elementos primários e subsequentes dos atributos, que são as funções de tais classes. Os atributos são seguidos das características
   principais das classes. ''')
p_3 = int(input('Digite o número correspondente a sua resposta: '))
gaba_user = [p_1, p_2, p_3]
print('')
print('RESULTADO FINAL')
if p_1 == 2:
    print('1 - Certo!')
else:
    print('1 - Errado!')
if p_2 == 3:
    print('2 - Certo!')
else:
    print('2 - Errado!')
if p_3 == 3:
    print('3 - Certo!')
else:
    print('3 - Errado!')