file = open("file.txt", 'r')
read_content = file.read()

values = []

for value in read_content.split('\n'):
  values.append(float(value))

print(f'A média é: {sum(values) / len(values)}')
file.close()
