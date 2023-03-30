nome=input('Digite seu nome: ')
idade=int(input('Digite seu nome: '))
d_contagiosa = input('Você tem alguma doença contagiosa? [S ou N]')

if (idade >= 65):
  print('Atendimento com prioridade')
  if (d_contagiosa == 'S'):
    print('Atendimento acontecerá na sala amarela')
  else:
    print('Atendimento acontecerá na sala branca')
else: 
  print('Atendimento sem prioridade')
  if (d_contagiosa == 'S'):
    print('Atendimento acontecerá na sala amarela')
  else:
    print('Atendimento acontecerá na sala branca')
