lista = []
with open('qp4.txt', 'w') as file:
  for i in range(10):
    lista.append(input(f'Digite o {i + 1}° valor: '))
  for name in lista:
    file.write(f'{name} \n')

for i, value in enumerate(lista):
  if (i != 0):
    if (value > lista[i - 1]):
      print(f'{value} É maior que o valor anterior({lista[i - 1]})')