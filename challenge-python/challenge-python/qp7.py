minutos_presente = int(input('Quantos minutos são para fabricar cada presente: '))
minutos_faltantes: int(input('Falta quantos minutos para você ir embora: '))

if (minutos_presente * 2 > minutos_faltantes):
  print('Você deve deixar o trabalho para amanhã')
else:
  print('Você conseguirá fabricar os presentes')
