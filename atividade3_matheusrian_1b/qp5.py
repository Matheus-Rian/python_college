def write(fileParam):
  names = []
  for i in range(6):
    names.append(input(f'Digite o {i + 1}° Nome e sobrenome: '))
  with open(fileParam, 'w') as file:
    for name in names:
      file.write(f'{name} \n')

def read(fileParam):
  with open(fileParam, 'r') as file:
    lines = file.readlines()
    for line in lines:
      print(line)

write('qp5.txt')
read('qp5.txt')