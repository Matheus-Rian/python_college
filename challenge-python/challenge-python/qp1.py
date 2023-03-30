while True:
  name = input('Digite seu nome: ')
  cont = 0

  if (name == 'SAIR' or cont == 10):
    break

  senha = input('Digite sua senha: ')
  situacao_mensalidade = input('Mensalidade OK [F ou P]: ')

  if (not(senha)):
    print('Seja bem-vindo(a)! Procure a recepção!')
  elif (situacao_mensalidade == 'P'):
    print(f'{name}, seja bem-vindo(a)!”')
  else:
    print(f'Não está esquecendo de algo, {name}? Procure a recepção!')