from functools import reduce

texto = [
    "hola",
    "me",
    "llamo",
    "amalia",
    "y",
    "me",
    "gustan",
    "las",
    "abejas",
    "y",
    "los",
    "arándanos"
]

palabras_con_a_inicial = [x.upper() if x[0] == 'a' else x for x in texto]

texto = reduce(lambda x, y: x + ' ' + y, palabras_con_a_inicial)
print(texto)
