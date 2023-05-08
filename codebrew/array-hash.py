amountOfFor = int(input())

for i in range(amountOfFor):
  sum = 0
  words = []
  letters = 'abcdefghijklmnopqrstuvwxyz'

  n = int(input())
  for i in range(n):
    words.append(input().lower())

  for index, word in enumerate(words):
    for i, w in enumerate(word):
      sum += word.index(w, i)
      sum += index
      sum += letters.index(letters[ord(w) - 97])

  print(sum)
