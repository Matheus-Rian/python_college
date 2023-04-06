vector = [3.5, 6.7, 1.0, 4.9]

vector.insert(1, 2.3)
print(vector)
vector.pop()
vector[2] = 9.2
vector.sort()
print(len(vector))

for i, v in enumerate(vector):
  print(f'indice {i}: {v}')