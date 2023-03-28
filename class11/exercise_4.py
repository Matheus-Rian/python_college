value = -1
sum = 0

while (value != 0):
  inputUser = int(input("Insira o valor do produto: "))
  if (inputUser == 0):
    value = 0
    print("programa encerrado.")
  else:
    if (inputUser > 0):
      sum+=inputUser
      print(sum)
  
  if (sum > 1000):
    sum = sum - sum * 0.1

print(sum)