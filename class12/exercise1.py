input_num = int(input('Digite um número: '))
acc = 0

for i in range(1, input_num):
  if (input_num % i == 0):
    acc += i

if (acc == input_num):
  print('Número perfeito')
else:
  print('Número imperfeito')
