matriz = []
average_salaray = 0
sum_transportation_vourcher = 0

for i in range(3):
  print()
  print(f'--- {i + 1} ESTAGIÁRIO(A)')
  salary = float(input('Digite seu salário: '))
  transportation_vourcher = float(input('Digite seu vale-transporte: '))
  alimentation_voucher = float(input('Digite seu vale-alimentação: '))
  matriz.append([salary, transportation_vourcher, alimentation_voucher])


for l in range(len(matriz)):
  average_salaray += matriz[l][0]
  sum_transportation_vourcher += matriz[l][1]

print()
print('Resultados finais: ')

for l in range(len(matriz)):
  for c in range(len(matriz[l])):
    print(matriz[l][c], end= ' ')
  print()

print(f'A média salarial foi: {average_salaray / 3}')
print(f'O total pago com o vale-transporte foi: {sum_transportation_vourcher}')
