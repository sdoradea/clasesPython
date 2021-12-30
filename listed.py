file = open("books.txt", "r")

listed = file.readlines()
relisted = []

for element in listed:
    relisted.append(element.strip())

for line in relisted:
  print(line[0] + str(len(line)))