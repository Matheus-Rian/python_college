keysWin = {
  'tesoura': ['papel', 'lagarto'],
  'pedra': ['tesoura', 'lagarto'],
  'papel': ['pedra', 'spock'],
  'spock': ['tesoura', 'pedra'],
  'lagarto': ['spock', 'papel']
}

amountOfFor = int(input())

for i in range(amountOfFor):
  values = input().split()

  if (values[0] == values[1]):
    print('empate')
  else:
    try:
      if (keysWin[values[0]].index(values[1]) >= 0):
        print('rajesh')
    except:
      print('sheldon')

