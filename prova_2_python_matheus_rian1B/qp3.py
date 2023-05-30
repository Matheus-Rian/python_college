n_celulas_tabuleiro = int(input('indique o número de células no tabuleiro: '))
valores_tabuleiro = []

for i in range(n_celulas_tabuleiro):
  valores_tabuleiro.append(int(input(f'Digite o {i + 1}º valor: ')))

def somar(esquerda, atual, direito):
  return esquerda + atual + direito

def campoMinado(valores):
  lista = []
  for i, value in enumerate(valores):
    if (i == 0):
      lista.append(somar(0, value, valores[i + 1]))
    elif ((i + 1) == len(valores)):
      lista.append(somar(valores[i - 1], value, 0))
    else:
      lista.append(somar(valores[i - 1], value, valores[i + 1]))
  
  return lista

for value in campoMinado(valores_tabuleiro):
  print(value)
