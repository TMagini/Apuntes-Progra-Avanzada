import os
from random import shuffle, choice
from collections import namedtuple


class Juego:

    def __init__(self, turnos):

        self.mazo = []
        self.cartas_j1 = []
        self.cartas_j2 = []

        self.read_file()
        self.repartir_cartas()
        self.comenzar_juego(turnos)

    def read_file(self):
        ruta_cartas = os.path.join('contenidos', 'semana-01', 'ejercicios_propuestos', 'cards.csv')
        with open(ruta_cartas, 'rt') as archivo:
            lineas = archivo.readlines()
            atributos = lineas[0].strip().split(',')
            Cartas = namedtuple('Cartas', atributos)
            for i in range(len(lineas[1:])):
                cartas = lineas[i].strip().split(',')
                self.mazo.append(Cartas(cartas[0], cartas[1], cartas[2]))

    def repartir_cartas(self):
        shuffle(self.mazo)
        while not (len(self.cartas_j1) and len(self.cartas_j2) == 5):
            self.cartas_j1.append(self.mazo.pop(0))
            self.cartas_j2.append(self.mazo.pop(0))

    def atacar(self, atacante, defensa):
        ptos_ataque = atacante.ataque
        ptos_defensa = defensa.defensa
        if ptos_ataque > ptos_defensa:
            return defensa

        else:
            return atacante

    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if i % 2:
                atacante = choice(self.cartas_j1)
                defensa = choice(self.cartas_j2)
                print(f'Juagador 1 ataca con {atacante.nombre}')
                perdedor = self.atacar(atacante, defensa)
                if perdedor == atacante:
                    print(f'Pierde el Jugador 1')
                    self.cartas_j1.remove(atacante)
                    self.cartas_j1.append(self.mazo.pop(0))
                else:
                    print(f'Pierde el Jugador 2')
                    self.cartas_j2.remove(defensa)
                    self.cartas_j2.append(self.mazo.pop(0))
            else:
                atacante = choice(self.cartas_j2)
                defensa = choice(self.cartas_j1)
                print(f'Juagador 2 ataca con {atacante.nombre}')
                perdedor = self.atacar(atacante, defensa)
                if perdedor == atacante:
                    print(f'Pierde el Jugador 2')
                    self.cartas_j2.remove(atacante)
                    self.cartas_j2.append(self.mazo.pop(0))
                else:
                    print(f'Pierde el Jugador 1')
                    self.cartas_j1.remove(defensa)
                    self.cartas_j1.append(self.mazo.pop(0))


juego = Juego(10)
