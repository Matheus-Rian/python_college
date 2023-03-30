preco_produto = 0
cont = 1
maior_preco = 0
menor_preco = 1000000

while cont <= 8:
  preco_produto = float('Digite o preço do produto: ')
  if (preco_produto > maior_preco):
    maior_preco = preco_produto
  
  if (preco_produto > menor_preco):
    menor_preco = preco_produto
  
  cont = cont + 1

print(f'O produto mais barato custa R$ {menor_preco}')
print(f'O produto mais caro custa R$ {maior_preco}')
