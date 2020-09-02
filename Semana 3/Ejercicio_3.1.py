from abc import ABC, abstractmethod


class Hamburgueseria(ABC):

    def __init__(self, clientes, stock):
        self.stock = stock
        self.clientes = clientes

    @abstractmethod
    def promedio_evaluaciones(self):
        pass

    def restar_stock(self):
        self.stock -= 1
        return self.stock

    def numero_clientes(self):
        return len(self.clientes)


class HamburgueseriaVegana:
    # recuerda que deben heredar

    def __init__(self, clientes, stock, evaluaciones_veggie):
        super().__init__(clientes, stock)
        self.evaluaciones_veggie = evaluaciones_veggie

    def promedio_evaluaciones(self):
        prom = sum(self.evaluaciones_veggie) / len(self.evaluaciones_veggie)
        return prom


class HamburgueseriaCarnivora:
    # recuerda que deben heredar

    def __init__(self, clientes, stock, evaluaciones_carnivora):
        super().__init__(clientes, stock)
        self.evaluaciones_carnivora = evaluaciones_carnivora

    def promedio_evaluaciones(self):
        prom = sum(self.evaluaciones_carnivora) / len(self.evaluaciones_carnivora)
        return prom
