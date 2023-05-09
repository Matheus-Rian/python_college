def returnNumberReverse(number):
  converterNumbertoString = str(number)
  return converterNumbertoString[::-1]

print(returnNumberReverse(int(input('Digite um número inteiro: '))))