matriz = []
sum_each_column = []

for i in range(3):
  print()
  print(f'--- números da linha {i + 1} ---')
  first_number = float(input('Digite o primeiro número: '))
  second_number = float(input('Digite o segundo número: '))
  third_number = float(input('Digite o terceiro número: '))
  matriz.append([first_number, second_number, third_number])

for value in matriz:
  sum_each_column.append(sum(value))

print(f'a soma dos números de cada coluna da matriz foi: {sum_each_column}')