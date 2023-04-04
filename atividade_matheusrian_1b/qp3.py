name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))
contagious_disease = input('Você tem alguma doença contagiosa (y/n): ')

if (age >= 65):
  print('Atendimento com prioridade')
else: 
  print('Atendimento sem prioridade')

if (contagious_disease == 'y'):
  print('Você será encaminhado para a sala amarela')
else:
  print('Você será encaminhado para a sala branca')