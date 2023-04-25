matriz = [[], [], []]
for l in range(3):
  for c in range(1):
    matriz[l].append(float(input('Digite sua nota da unidade1: ')))
    matriz[l].append(float(input('Digite sua nota da unidade2: ')))
    matriz[l].append(float(input('Digite sua frequência: ')))

print('---TABELA---')
for l in range(3):
  for c in range(3):
    print(matriz[l][c], end=" ")
  print()
print('------')

soma = 0
for i in range(3):
  soma += matriz[i][0]

print(f'A média das notas na unidade1 foi: {soma / 3}')

