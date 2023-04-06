answers = []

answers.append(input('Conhece a vítima do furto?'))
answers.append(input('Esteve no local do furto?'))
answers.append(input('Mora perto da vítima?'))
answers.append(input('A vítima lhe devia?'))
answers.append(input('Já trabalhou com a vítima?'))
cont = 0

for answer in answers:
  if (answer == 'S'):
    cont += 1

if (cont < 2):
  print('Inocente')
elif (cont == 2):
  print('Suspeito')
elif (cont <= 4):
  print('Cúmplice')
else:
  print('Ladrão')
