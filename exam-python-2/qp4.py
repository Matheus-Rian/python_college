total_votos = 0
vetor_camisas_votos = [0, 0, 0, 0, 0, 0]

while True:
  numero_camisa_jogador = int(input('Digite o número da camisa de 1 a 6 (0 - Encerrar programa): '))
  if (numero_camisa_jogador == 0):
    break

  if (numero_camisa_jogador > 6 or numero_camisa_jogador < 1):
    print('Número inválido!')
  else:
    print(f'{numero_camisa_jogador}')
    total_votos += 1
    if (numero_camisa_jogador == 1):
      vetor_camisas_votos[0] += 1
    elif (numero_camisa_jogador == 2):
      vetor_camisas_votos[1] += 1
    elif (numero_camisa_jogador == 3):
      vetor_camisas_votos[2] += 1
    elif (numero_camisa_jogador == 4):
      vetor_camisas_votos[3] += 1
    elif (numero_camisa_jogador == 5):
      vetor_camisas_votos[4] += 1
    elif (numero_camisa_jogador == 6):
      vetor_camisas_votos[5] += 1

print('--- Resultados ---')
print(f'Total de votos computados: {total_votos}')

for i in range(6):
  if (vetor_camisas_votos[i] > 0):
    print(f'jogador com a camisa {i + 1} recebeu {vetor_camisas_votos[i]} votos. porcentagem foi de {vetor_camisas_votos[i] * 100 / total_votos}')

melhor_jogador = max(vetor_camisas_votos)
for i in range(6):
  if (melhor_jogador == vetor_camisas_votos[i]):
    print()
    print('Jogador da partida: ')
    print(f'O melhor jogador foi o camisa {i + 1}. Recebeu {vetor_camisas_votos[i]} votos. porcentagem foi de {vetor_camisas_votos[i] * 100 / total_votos}')
