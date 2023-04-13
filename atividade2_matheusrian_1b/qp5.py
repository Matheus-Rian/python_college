amount_mouses = int(input('Quantidade de mouses: '))
amount_defects_per_type = [0, 0, 0, 0]

for i in range(amount_mouses):
  print('------')
  id = input(f'Digite o identificador do {i + 1} mouse: ')
  print('Digite o número do defeito: ')
  defect = int(input(
      "\n 1 - necessita da esfera \n 2 - necessita de limpeza \n 3 - necessita troca do cabo ou conector \n 4 - quebrado ou inutilizado \n"
    ))
  
  if (defect == 1):
    amount_defects_per_type[0] += 1
  elif (defect == 2):
    amount_defects_per_type[1] += 1
  elif (defect == 3):
    amount_defects_per_type[2] += 1
  elif (defect == 4):
    amount_defects_per_type[3] += 1
  else:
    print('Valor inválido')

print(f'Quantidade de mouses: {amount_mouses}')
print('Situação                                     Quantidade                   Percentual')
print(f'1 - necessita da esfera                                   {amount_defects_per_type[0]}                  {amount_defects_per_type[0] / amount_mouses * 100}%')
print(f'2 - necessita de limpeza                                  {amount_defects_per_type[1]}                  {amount_defects_per_type[1] / amount_mouses * 100}%')
print(f'3 - necessita troca do cabo ou conector                   {amount_defects_per_type[2]}                  {amount_defects_per_type[2] / amount_mouses * 100}%')
print(f'4 - quebrado ou inutilizado                               {amount_defects_per_type[3]}                  {amount_defects_per_type[3] / amount_mouses * 100}%')


