#entrada = int(input())
#anos_int = entrada // 365
#anos_rest = entrada % 365
#meses_int = anos_rest // 30
#meses_rest = anos_rest % 30
#dias_int = meses_rest // 1
#print('{} ano(s)'.format(anos_int))
#print('{} mes(es)'.format(meses_int))
#print('{} dia(s)'.format(dias_int))

entrada = int(input())
horas = entrada / 3600
minutos = entrada / 60
segundos = entrada % 60
lista = [horas, minutos,segundos]
print('{:.0f}:{:.0f}:{:.0f}'.format(horas, minutos, segundos))