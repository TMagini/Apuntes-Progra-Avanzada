from string import ascii_lowercase as letras

print(letras)

consonantes = dict()

consonantes = {letras[i]: i for i in range(len(letras)) if i % 3 != 0 or i == 0}
print(consonantes)
