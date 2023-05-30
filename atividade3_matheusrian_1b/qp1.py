try:
  listNumbers = []
  higher = 0
  smallest = 0
  equal = 0

  for i in range(10):
    listNumbers.append(int(input(f'Digite o {i + 1}° número: ')))
  
  firstElement = listNumbers[0]
  listNumbers.pop(0)

  for value in listNumbers:
    if value > firstElement:
      higher += 1
    elif value < firstElement:
      smallest += 1
    else:
      equal += 1

  print('Quantidade de: ')
  print(f'maiores: {higher}')
  print(f'menores: {smallest}')
  print(f'Iguais: {equal}')
except:
  print('Valor inválido!')