from datetime import date

for i in range(5):
  year_birth = int(input('Digite o ano do seu nascimento: '))
  if (date.today().year - year_birth >= 18):
    print('É adulto')
  else:
    print('Não é adulto')