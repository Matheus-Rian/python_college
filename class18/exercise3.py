def statusOfStudent(note):
  if (note > 6):
    return 'Aprovado'
  if (note >= 4 and note <= 6):
    return 'Verificação Suplementar'
  
  return 'Reprovado'

def averageOfStudent(n1, n2):
  return statusOfStudent((n1 + n2) / 2)

status = averageOfStudent(int(input('Nota n1: ')), int(input('Nota n2: ')))
print(status)