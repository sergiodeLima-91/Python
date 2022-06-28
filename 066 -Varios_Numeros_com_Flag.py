# Crie um programa que leia vários números inteiros e pare somente com um flag de nome 999. O programa
# deve mostrar a quantidade de números inteiros digitados pelo usuário e qual a soma entre eles (sem o flag)

n = s = cont = 0 # Necessário declarar a variável antes porque o teste lógico é realizado logo de início pelo while.
while n != 999:
    n = int(input('Digite qualquer número inteiro: '))
    if n == 999:   # Necessário usar break para que o flag (999) não seja considerado na soma de todos os números
        break      # inteiros inseridos pelo usuário na variável 'n'.
    s += n # Essa variável é usada para somar os números. O que ocorre é justamente a soma do valor que existe em
           # 's' com o valor digitado pelo usuário e armazenado em 'n'. O processo se repete.
    cont += 1 # Se esta estrutura aqui estivesse acima do "if" o flag iria ser contado na soma dos termos digitados.
print(f'A soma total dos termos é de {s}')
print(f'O número total de termos digitados foi de {cont}')