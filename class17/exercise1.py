from random import randint

numbersRandom = []

for i in range(5):
  numbersRandom.append(randint(0, 100))

tupleNumbers = tuple(numbersRandom)

print(numbersRandom)
print(f'o maior número é {max(tupleNumbers)}')
print(f'o menor número é {min(tupleNumbers)}')
