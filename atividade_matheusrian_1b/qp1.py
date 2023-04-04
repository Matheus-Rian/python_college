newest_car = 0
amount_cars = 0
fastest_car = 0

while True:
  year = input('Digite o ano do carro: ')
  velocity = input('Digite a velocidade do carro: ')

  if (year == 'N' or velocity == 'N'):
    print(
      f' Quantidade de carros: {amount_cars}\n', 
      f'O carro mais novo: {newest_car}\n', 
      f'O carro mais rápido: {fastest_car}\n'
    )
    break
  else:
    amount_cars += 1

    if (int(year) > newest_car):
      newest_car = int(year)
    
    if (int(velocity) > fastest_car):
      fastest_car = int(velocity)

