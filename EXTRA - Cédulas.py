entrada = int(input())
print(entrada)
cem_int = entrada // 100
cem_rest = entrada % 100
cinq_int = cem_rest // 50
cinq_rest = cem_rest % 50
vinte_int = cinq_rest // 20
vinte_rest = cinq_rest % 20
dez_int = vinte_rest // 10
dez_rest = vinte_rest % 10
cinco_int = dez_rest // 5
cinco_rest = dez_rest % 5
dois_int = cinco_rest // 2
dois_rest = cinco_rest % 2
um_int = dois_rest // 1

print(f'{cem_int} nota(s) de R$ 100,00')
print(f'{cinq_int} nota(s) de R$ 50,00')
print(f'{vinte_int} nota(s) de R$ 20,00')
print(f'{dez_int} nota(s) de R$ 10,00')
print(f'{cinco_int} nota(s) de R$ 5,00')
print(f'{dois_int} nota(s) de R$ 2,00')
print(f'{um_int} nota(s) de R$ 1,00')