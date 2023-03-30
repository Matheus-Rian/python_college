while True:
  cont = 1
  valorTotal = float(input('Valor total da Confraternização: '))
  numero_func = int(input('Quantos funcionários participaram: '))
  somaTotal = 0
  media = 0
  maiorValor = 0
  melhorPagador = ''

  while cont <= numero_func:
    nome = input('Digite seu nome: ')
    valorPago = int(input('Quanto deseja pagar: '))

    somaTotal += valorPago
    if (valorPago > maiorValor):
      melhorPagador = nome
      maiorValor = valorPago

    cont += 1

  media = somaTotal / numero_func

  print(f'O valor da conta foi: {valorTotal}')
  print(f'A média dos valores foi: {media}')
  print(f'A pessoal que pagou mais foi: {melhorPagador}')
  print(f'O excedente que será pago: {maiorValor - media}')
  break
