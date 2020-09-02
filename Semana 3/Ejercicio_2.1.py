class Burro:
    """Clase de Burro"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cancion = "Estoy solito, no hay nadie aqui a mi lado (8)"

    def cantar(self):
        print(self.cancion)


class Dragona:
    """Clase de Dragona"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fuego = "Estoy escupiendo fuego"

    def escupir_fuego(self):
        print(self.fuego)


class HijoBurro(Burro, Dragona):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
