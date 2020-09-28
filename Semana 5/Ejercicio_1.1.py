def es_primo(nr):
    if nr > 1:
        for i in range(2, nr):
            if not (nr % i):
                return False
        return True
    return False


class IterablePrimos:

    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def __iter__(self):
        lista_primos = []
        contador = self.inicio
        while contador <= self.fin:
            if es_primo(contador):
                lista_primos.append(contador)
            contador += 1

        return iter(IteradorPrimos(lista_primos))


class IteradorPrimos:

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont <= (len(self.iterable) - 1):
            valor = self.iterable[self.cont]
            self.cont += 1
            return valor

        else:
            raise StopIteration("Llegamos al final")


iterable_primos = IterablePrimos(1, 25)
for i in iterable_primos:
    print(i)
