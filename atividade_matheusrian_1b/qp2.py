tree_value = float(input('Digite o valor da árvore: '))
amount_ornaments = int(input('Quantidade de enfeites: '))
price_unit_ornament = float(input('Preço unitário de cada um: '))

value_total = tree_value + price_unit_ornament * amount_ornaments

print(f'O valor a ser pago por cada funcionário será {value_total / 20}')