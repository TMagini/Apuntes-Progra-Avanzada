import os
from random import shuffle, choice


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
            self.mazo = [x.strip().split(',') for x in lineas[1:]]

    def repartir_cartas(self):
        shuffle(self.mazo)
        while not (len(self.cartas_j1) and len(self.cartas_j2) == 5):
            self.cartas_j1.append(self.mazo.pop(0))
            self.cartas_j2.append(self.mazo.pop(0))

    def atacar(self, atacante, defensa):
        ptos_ataque = atacante[1]
        ptos_defensa = defensa[2]
        if ptos_ataque > ptos_defensa:
            return atacante
        else:
            return defensa

    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if i % 2:
                ataque_J1 = choice(self.cartas_j1)
                defensa_J2 = choice(self.cartas_j2)
                print(f'Juagador 1 ataca con {ataque_J1[0]}')
                perdedor = self.atacar(ataque_J1, defensa_J2)
                if perdedor in self.cartas_j1:
                    print(f'Pierde el Jugador 1')
                    self.cartas_j1.remove(ataque_J1)
                    self.cartas_j1.append(self.mazo.pop(0))
                else:
                    print(f'Pierde el Jugador 2')
                    self.cartas_j2.remove(defensa_J2)
                    self.cartas_j2.append(self.mazo.pop(0))

            else:
                ataque_J2 = choice(self.cartas_j2)
                defensa_J1 = choice(self.cartas_j1)
                print(f'Juagador 2 ataca con {ataque_J2[0]}')
                perdedor = self.atacar(ataque_J2, defensa_J1)
                if perdedor in self.cartas_j2:
                    print(f'Pierde el Jugador 2')
                    self.cartas_j2.remove(ataque_J2)
                    self.cartas_j2.append(self.mazo.pop(0))
                else:
                    print(f'Pierde el Jugador 1')
                    self.cartas_j1.remove(defensa_J1)
                    self.cartas_j1.append(self.mazo.pop(0))


juego = Juego(10)
