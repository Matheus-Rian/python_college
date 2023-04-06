notes = []

for i in range(5):
  notes.append(float(input(f'Digite a sua nota: ')))

average_class = sum(notes) / len(notes)

for i, v in enumerate(notes):
  if (notes[i] > average_class):
    print(f'A nota do aluno {i}, está acima da média da turma {average_class}')