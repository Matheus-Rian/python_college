a = []
b = []
c = []
average_odd = []
sum_pair = []
smaller_value_c = 0 

for i in range(5):
  a.append(int(input(f'Adicione o {i + 1} número do primeiro(a) vetor: ')))

for i in range(5):
  a.append(int(input(f'Adicione o {i + 1} número do segundo(b) vetor: ')))

c = a + b
smaller_value_c = c[0]

for value in c:
  if value % 2 == 0:
    sum_pair.append(value)
  else: 
    average_odd.append(value)
  
  if value < smaller_value_c:
    smaller_value_c = value

print(f'A média dos números impares foi: {sum(average_odd) / len(average_odd)}')
print(f'A soma dos números pares foi: {sum(sum_pair)}')
print(f'O menor valor de C foi: {smaller_value_c}')

