try:
  users = {}
  for i in range(2):
    name = input('Digite seu nome: ')
    likes = input('Digite a quantidade de curtidas das últimas TRÊS fotos (Ex: 20, 20, 20) : ')

    users[name] = {
      'likes': likes.split(','),
      'average': 0
    }

  for key, value in users.items():
    for like in value['likes']:
      users[key]['average'] += int(like)
    users[key]['average'] = users[key]['average'] / len(users[key]['likes'])

  higherUser = ''
  higherAverage = 0
  for key, value in users.items():
    if (value['average'] > higherAverage):
      higherAverage = value["average"]
      higherUser = f'{key.capitalize()} teve a maior média {value["average"]}'

  print(higherUser)
  del users[higherUser.split()[0].lower()]

  for key, value in users.items():
    print(f'{key} tem uma média de {value["average"]}')
except:
  print('Valor inválido')