
matriz = [[], [], []]
diagonal_principal = 0
media = 0
maior = 0
menor_ou_igual_media = []

for l in range(3):
  for c in range(3):
    matriz[l].append(int(input('Digite um número: ')))

for index, value in enumerate(matriz):
  
  if index == 0:
    diagonal_principal = value[0]
  elif index == 1:
    diagonal_principal = value[1]
  else: 
    diagonal_principal *= value[2]

print(matriz)

for values in matriz:
  media += sum(values)

media = media / 9
print(media)

for l in range(3):
  for c in range(3):
    if (matriz[l][1] > maior):
      maior = matriz[l][1]

print(maior)

for l in range(3):
  for c in range(3):
    if (matriz[l][c] <= media):
      menor_ou_igual_media.append(matriz[l][c])
  
print(menor_ou_igual_media)