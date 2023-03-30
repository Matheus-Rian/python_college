reta_a = float(input('Digite o valor do primeiro segmento de reta: '))
reta_b = float(input('Digite o valor do segundo segmento de reta: '))
reta_c = float(input('Digite o valor do terceiro segmento de reta: '))

if (reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_c + reta_b > reta_a):
  print('É possível formar um triângulo com esses segmentos')
else:
  print('Não é possível formar um triângulo com esses segmentos')
  