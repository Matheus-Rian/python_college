numberInitial = int(input("Número inicial: "))
numberFinish = int(input("Número final: "))
numberActual = numberInitial

while (numberActual <= numberFinish):
  if (numberActual % 2 == 0):
    print(numberActual)

  numberActual+=1
