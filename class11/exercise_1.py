yearOfAdmission = int(input("Ano de admissão: "))
actualSalary = float(input("Salário atual: "))
yearOfLastSalaryAdjustment = int(input("Ano do último reajuste salarial: "))
timeOfHouse = 2023 - yearOfAdmission

if (timeOfHouse < 5 and (2023 - yearOfLastSalaryAdjustment) >= 2):
  print('Entrei no 1')
  print(f'Seu novo salário é: {actualSalary + actualSalary * 0.1}')
elif (timeOfHouse > 10 and (2023 - yearOfLastSalaryAdjustment) >= 2):
  print(f'Seu novo salário é: {actualSalary + actualSalary * 0.3}')
  print('Entrei no 2')
elif ((2023 - yearOfLastSalaryAdjustment) >= 2):
  print('Entrei no 3')
  print(f'Seu novo salário é: {actualSalary + actualSalary * 0.2}')
else:
  print("Infelizmente você não está apto para receber o reajuste salarial")

