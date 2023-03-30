c=0
media=0
somaidade = 0

while True:
    idade=int(input("Digite sua idade: "))
    if idade==999:
      print(f"quantidade de alunos é {c}")
      media = somaidade / c
      print(f'A média é: {media}')
      break
    
    else:
      c+=1
      somaidade += idade
