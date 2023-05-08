amountOfWords = int(input())

for i in range(amountOfWords):
  word = input()
  wordDecrypted = ''

  for value in word.split('·'):
    wordDecrypted += value[0]
  
  print(wordDecrypted)