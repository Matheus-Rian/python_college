team1 = input('Digite o nome da primeira equipe: ')
team2 = input('Digite o nome da segunda equipe: ')

num_goals1 = int(input('Digite o número de gols da primeira equipe: '))
num_goals2 = int(input('Digite o número de gols da segunda equipe: '))

if (num_goals1 > num_goals2):
  print(f'A equipe vencedora foi: {team1}')
elif (num_goals2 > num_goals1):
  print(f'A equipe vencedora foi: {team2}')
else:
  print('EMPATE!')
