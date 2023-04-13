amount_number = int(input('quantos elementos da sequência de Fibonacci gostaria de visualizar: '))
fibonacci = [1, 1]
showFibonacci = ''

for i in range(0, amount_number - 2):
  if (len(fibonacci) > 2):
    del fibonacci[0]
  
  showFibonacci += f'{sum(fibonacci)} '
  fibonacci.append(sum(fibonacci))

print(f'1 1 {showFibonacci}')