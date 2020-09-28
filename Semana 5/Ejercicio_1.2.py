generador_serie_armonica = (1 / i for i in range(1, 11))
generador_serie_armonica = tuple(generador_serie_armonica)

for i in generador_serie_armonica:
    print(i)

print(sum(generador_serie_armonica))
