from time import sleep
from random import  choice

import emoji

print('=-=' * 16)
print('\033[1;34mT  I  R  A  N  D  O    S  U  A    M  É  D  I  A\033[m')
print('=-=' * 16)
n1 = float(input('Digite  a \033[1;33mprimeira nota\033[m:  '))
n2 = float(input('Digite a \033[1;35msegunda nota\033[m:  '))
loading = ['Que ruflem os tambores!', 'E o resultado é...', 'Só um minuto, meu querido(a)...']
escolha = choice(loading)
print(escolha)
sleep(2)
media = (n1 + n2) / 2
print('Sua média final foi {}.'.format(media))
if media < 5:
    print('Sinto muito, mas você foi \033[1;31mREPROVADO!\033[m')
elif media == 10:
    print(emoji.emojize('😁 \033[1;032m🎉🎉 Meus PARABÉNS por tirar a média máxima!Passe na secretaria e pegue seu prêmio! 🎉🎉\033[m 😁', language='pt'))
elif media >= 7:
    print('Parabéns! Você foi \033[1;032mAPROVADO (A)!\033[m')
else:
    print('Será possível melhorar ainda mais sua nota! Você está de \033[1;33mRECUPERAÇÃO!')
print()
print(emoji.emojize('Até mais!:rosto_com_olho_piscando:', language='pt'))

# Tecla de atalho para a lista de emojis do windows: Windows + . (ponto)
# Código atualizado em 29/07/2022