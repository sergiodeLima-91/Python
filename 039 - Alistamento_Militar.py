print("-=-" * 19)
print('\033[1;32mA  L  I  S  T  A  M  E  N  T  O     M  I  L  I  T  A  R\033[m')
print('-=-' * 19)
idade = int(input('Qual é a sua \033[1;31midade? '))
restante = 18 - idade
ultrapassado = idade - 18
if idade == 18:
    print('\033[32mEste é o momento exato de alistar-se no serviço militar! Dirija-se até a junta mais próxima de sua cidade!\033[m')
elif ultrapassado >= 2:
    print(f'\033[31mVocê está ABSURDAMENTE atrasado em {ultrapassado} anos! Aliste-se AGORA MESMO!')
elif idade > 18:
    print(f'\033[33mVocê já ultrapassou a data de alistamento em {ultrapassado} ano! Corra! Está atrasado!')
else:
    print(f'\033[32mFalta (m) {restante} ano (s) para que você possa alistar-se no serviço militar. Aguarde!')

# Última atualização do código em 29/07/2022.