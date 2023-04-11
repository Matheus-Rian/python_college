amount_products = int(input('Quantidade de produtos vendidos: '))
weights = []
sum_weights = 0
greater_weight = 0
smaller_weight = 100

for i in range(0, amount_products):
  weights.append(float(input(f'Qual o peso do {i + 1} produto: ')))

for weightActual in weights:
  if (weightActual > greater_weight):
    greater_weight = weightActual
  elif (weightActual < smaller_weight):
    smaller_weight = weightActual

  sum_weights += weightActual

print(f'O peso médio é {sum_weights / amount_products}')
print(f'O maior peso é {greater_weight}')
print(f'O menor peso é {smaller_weight}')
print(f'No dia foi arrecadado {sum_weights * 4.35}')
