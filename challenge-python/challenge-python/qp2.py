while True:
  num = int(input('Digite um número: '))
  if (num == -1):
    break
  if (num < 7):
    print('ACIDA')
  elif (num > 7):
    print('BÁSICA')
  else: 
    print('NEUTRA')