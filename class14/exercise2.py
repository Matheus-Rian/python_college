while True:
  name = input('Digite o nome do atleta: ')
  heels = []

  if (name.lower() == 'sair'):
    break

  for i in range(1, 6):
    heels.append(float(input(f'Digite a distância alcançada no {i} salto: ')))
  
  print(f'nome: {name}')
  for i in range(len(heels)):
    print(f'{i + 1} Salto: {heels[i]} m')
  
  print(f'A média dos saltos: {sum(heels) / len(heels)}')