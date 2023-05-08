amountOfLedsPerNumber = {
  '1': 2,
  '2': 5,
  '3': 5,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 3,
  '8': 7,
  '9': 6,
  '0': 6,
}

amountOfNumbers = int(input())
numbers = []

for i in range(amountOfNumbers):
  numbers.append(input())

for number in numbers:
  sum = 0
  for n in number:
    sum = sum + amountOfLedsPerNumber[n]

  print(f'{sum} leds')


