linha_torre = int(input('Digite a linha que a torre se encontra: '))
coluna_torre = int(input('Digite a coluna que a torre se encontra: '))

matriz = [[], [], [], [], [], [], [], []]

for l in range(8):
  for c in range(8):
    matriz[l].append('-')

print()
print('--- TABULEIRO DE XADREZ ---')
for l in range(8):
  for c in range(8):
    if ((l + 1) == linha_torre):
      matriz[l][c] = 'X'

    if ((c + 1) == coluna_torre):
      for i in range(8):
        matriz[i][c] = 'X'
    print(matriz[l][c], end=" ")
  print()
