phrase = input('Digite uma frase: ')
qtdE = phrase.count('e')

print(f'A quantidade de palavras é: {len(phrase.split())}')
if (qtdE):
  print(f'A quantidade de letras "e" é: {qtdE}')
else: 
  print(f'A quantidade de letras "e": Não existe')
print(f'A terceira palavra da frase é: {phrase.split()[2]}')
