vetor = []
vetor_decrescente = []
valor_mais_alto_atual = 0

quant_numeros = int(input('Digite a quantidade de números que deseja ordernar em ordem decrescente: '))
for i in range(quant_numeros):
  vetor.append(int(input(f'Digite o {i + 1} número: ')))

tamanho_vetor = len(vetor)

for i in range(tamanho_vetor):
  valor_mais_alto_atual = max(vetor)
  vetor_decrescente.append(valor_mais_alto_atual)

  for index, value in enumerate(vetor):
    if valor_mais_alto_atual == value:
      vetor[index] = 0

print(vetor_decrescente)