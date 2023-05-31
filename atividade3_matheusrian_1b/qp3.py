try:
  lista = []
  with open('qp3.txt', 'w') as file:
    for i in range(6):
      lista.append(input(f'Digite o {i + 1}° nome: '))
    for name in lista:
      file.write(f'{name} \n')

  with open('qp3Order.txt', 'w') as file:
    for nameSort in sorted(lista):
      file.write(f'{nameSort} \n')
except:
  print('Algo inesperado aconteceu, tente novamente!')