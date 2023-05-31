with open('qp2.txt', 'r') as file:
  lines = file.readlines()
  for value in lines:
    higherThan255 = 0

    for v in value.split('.'):
      if (int(v) > 255):
        higherThan255 += 1

    if higherThan255:
      print(f'{value} é inválido')
    else: 
      print(f'{value} é válido')