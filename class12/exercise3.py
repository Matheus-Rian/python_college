import math

equation_qtd = int(input('Quantas equações deseja calcular'))

def bhaskaraPositive(b, delta, a):
  return (-b + math.sqrt(delta)) / 2 * a

def bhaskaraNegative(b, delta, a):
  return (-b - math.sqrt(delta)) / 2 * a

for i in range(0, equation_qtd):
  num_a = int(input('Digite o valor de a: '))
  if (num_a != 0):
    num_b = int(input('Digite o valor de b: '))
    num_c = int(input('Digite o valor de c: '))

    delta = num_b**2 - 4 * num_a * num_c
    if (delta == 0):
      print(bhaskaraPositive(num_b, delta, num_a))
    elif (delta > 0):
      print(bhaskaraPositive(num_b, delta, num_a))
      print(bhaskaraNegative(num_b, delta, num_a))

