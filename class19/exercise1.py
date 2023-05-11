
def sum(a, b):  
  return a + b

def subtraction(a, b):  
  return a - b

def multiple(a, b):  
  return a * b

def division(a, b):
  if a > b:
    return a / b
  return b / a

a = int(input())
operation = input('Qual operacão deseja fazer (+ , - , *, /): ')
b = int(input())

calcs = {
  '+': sum(a, b),
  '-': subtraction(a, b),
  '/': division(a, b),
  '*': multiple(a, b)
}

print(calcs[operation])


