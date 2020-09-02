# GrandPrix

class GrandPrix:

    def __init__(self):
        self.competidores = None  # list[Piloto]
        self.pista = None  # Pista
        self.posibles_pistas = None  # list[Pista]
        self.vehiculos = None  # list[Vehiculo]

    def cargar_competidores(self):
        pass

    def elegir_pista(self):
        pass

    def iniciar_carrera(self):
        pass

# Vehiculos


class Vehiculo:

    def __init__(self):
        self.nombre = None  # str
        self.combustible_restante = None  # int
        self.estado_neumaticos = None  # int
        self.aceleracion = None  # int

    def ir_a_los_pits(self):
        pass


class AutoFormula1(Vehiculo):

    def __init__(self):
        super().__init__()
        self.aleron = None  # int

    def adelantado_rapido(self):
        pass


class Camion(Vehiculo):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fuerza = None  # int

    def chocar(self):
        pass


class AutoRally(Vehiculo):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.traccion = None  # int

    def derrapar(self):
        pass


class MonsterTruck(Camion, AutoRally):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.peso = None  # int

# Pilotos


class Piloto:

    def __init__(self):
        self.nombre = None  # str
        self.habilidad = None  # int
        self.vehiculos = None  # list


class Usuario(Piloto):

    def __init__(self):
        super().__init__()
        self.experiencia = None  # int

    def elegir_vehiculo(self):
        pass


class Contrincante(Piloto):

    def __init__(self):
        super().__init__()
        self.nivel = None  # int

# Pista


class Pista:

    def __init__(self):
        self.nombre = None  # str
        self.dificultad = None  # int
        self.numero_de_vueltas = None  # int
