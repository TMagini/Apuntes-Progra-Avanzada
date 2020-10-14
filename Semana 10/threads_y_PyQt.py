from os import path
from random import randint
from time import sleep

from PyQt5.QtCore import pyqtSignal, QTimer, QObject, QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton, QMainWindow)

# Ejemplo de ventana con threading pero con el modulo QThread

'''
class MiThread(QThread):

    # Se define para la clase MiThread,
    # para que cada instancia tenga una propia
    senal_actualizar = pyqtSignal(int, str)

    def __init__(self, i, tiempo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.indice = i
        self.tiempo = tiempo

    def run(self):
        for i in range(10):
            sleep(self.tiempo)
            self.senal_actualizar.emit(self.indice, str(i))
        self.senal_actualizar.emit(self.indice, 'Status: thread terminado')


class MiVentana(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threads = []
        self.init_gui()

    def init_gui(self):
        # Configuramos los widgets de la interfaz
        # Definimos un montón de labels que corresponderán a un thread cada uno
        self.labels = {
            i: QLabel('Status: esperando thread', self)
            for i in range(1, 6)
        }
        self.boton = QPushButton('Ejecutar Threads', self)
        self.boton.clicked.connect(self.ejecutar_threads)

        hboxs = []
        for i in range(1, 6):
            hbox = QHBoxLayout()
            hbox.addStretch(1)
            hbox.addWidget(self.labels[i])
            hbox.addStretch(1)
            hboxs.append(hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton)
        hbox.addStretch(1)
        hboxs.append(hbox)

        vbox = QVBoxLayout()
        for hbox in hboxs:
            vbox.addStretch(1)
            vbox.addLayout(hbox)
            vbox.addStretch(1)
        self.setLayout(vbox)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle('Ejemplo threads')
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def ejecutar_threads(self):
        """
        Este método crea cinco threads cada vez que se presiona el botón en la
        interfaz. Los threads recibirás como argumento el índice del label 
        que les corresponde y el tiempo que toman entre cada iteración.
        """
        if len(self.threads) == 0 or not any([thread.isRunning() for thread in self.threads]):
            self.threads = []
            for i in range(1, 6):
                thread = MiThread(i, i / 10)
                # Se conecta la señal emitida por el thread a un método
                # de la ventana
                thread.senal_actualizar.connect(self.actualizar_labels)
                self.threads.append(thread)
                thread.start()

    def actualizar_labels(self, indice, texto):
        """
        Este método actualiza el label correspondiente según los datos 
        enviados desde un thread através del índice y aplica el texto.
        """
        self.labels[indice].setText(texto)


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())
'''

# Ejemplo con QTimer

'''
class MiTimer(QObject):

    senal_actualizar = pyqtSignal(int, str)

    def __init__(self, i, tiempo):
        super().__init__()
        self.indice = i
        self.tiempo = tiempo
        self.indice_actual = 0
        self.timer = QTimer()
        self.timer.setInterval(tiempo * 1000)
        self.timer.timeout.connect(self.enviar_dato)

    def enviar_dato(self):
        if self.indice_actual < 9:
            self.senal_actualizar.emit(self.indice, str(self.indice_actual))
            self.indice_actual += 1
        else:
            self.senal_actualizar.emit(self.indice, 'Status: timer terminado')
            self.timer.stop()

    def comenzar(self):
        self.timer.start()

    def sigue_andando(self):
        return self.timer.isActive()


class MiVentana(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timers = []
        self.init_gui()

    def init_gui(self):
        # Configuramos los widgets de la interfaz
        # Definimos un montón de labels que corresponderán a un timer cada uno
        self.labels = {
            i: QLabel('Status: esperando timer', self)
            for i in range(1, 6)
        }
        self.boton = QPushButton('Ejecutar Timers', self)
        self.boton.clicked.connect(self.ejecutar_timers)

        hboxs = []
        for i in range(1, 6):
            hbox = QHBoxLayout()
            hbox.addStretch(1)
            hbox.addWidget(self.labels[i])
            hbox.addStretch(1)
            hboxs.append(hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton)
        hbox.addStretch(1)
        hboxs.append(hbox)

        vbox = QVBoxLayout()
        for hbox in hboxs:
            vbox.addStretch(1)
            vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle('Ejemplo timers')
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def ejecutar_timers(self):
        """
        Este método crea cinco threads cada vez que se presiona el botón en la
        interfaz. Los threads recibirás como argumento el índice del label 
        que les corresponde y el tiempo que toman entre cada iteración.
        """
        if len(self.timers) == 0 or not any([timer.sigue_andando() for timer in self.timers]):
            self.timers = []
            for i in range(1, 6):
                timer = MiTimer(i, i / 10)
                # Se conecta la señal emitida por el timer
                # a un método de la ventana
                timer.senal_actualizar.connect(self.actualizar_labels)
                self.timers.append(timer)
                timer.comenzar()

    def actualizar_labels(self, indice, texto):
        """
        Este método actualiza el label correspondiente según los datos 
        enviados desde un thread através del índice y aplica el texto.
        """
        self.labels[indice].setText(texto)


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())
'''

# Ejemplo de QThread

class Comida(QThread):

    actualizar = pyqtSignal(QLabel, int, int)

    def __init__(self, parent, limite_x, limite_y):
        """
        Una Comida es un QThread que movera una imagen de comida
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            limite_x e limite_y: Los límites rectangulares de la ventana
        """
        super().__init__()

        # Guardamos el path de la imagen que tendrá el Label
        self.ruta_imagen = path.join("Semana 10", "img", "food", f"{randint(1, 9)}.png")

        # Creamos el Label y definimos su tamaño
        self.label = QLabel(parent)
        self.label.setGeometry(-50, -50, 50, 50)
        self.label.setPixmap(QPixmap(self.ruta_imagen))
        self.label.setScaledContents(True)
        self.label.setVisible(True)

        # Guardamos los limites de la ventana para que no pueda salirse de ella
        self.limite_x = limite_x
        self.limite_y = limite_y
        # Seteamos la posición inicial y la guardamos para usarla como una property
        self.__posicion = (0, 0)
        self.posicion = (randint(0, limite_x), randint(0, limite_y))

        self.label.show()
        self.start()

    @property
    def posicion(self):
        return self.__posicion

    # Cada vez que se actualicé la posición,
    # se actualiza la posición de la etiqueta
    @posicion.setter
    def posicion(self, valor):
        self.__posicion = valor
        self.actualizar.emit(self.label, *self.posicion)

    def run(self):
        while self.posicion[0] < self.limite_x and self.posicion[1] < self.limite_y:
            sleep(0.1)
            nuevo_x = self.posicion[0] + 1
            nuevo_y = self.posicion[1] + 1
            self.posicion = (nuevo_x, nuevo_y)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 500)
        self.show()

        # Contador de cuanta comida hemos creado
        self.comida_creada = 0

        # Creamos un Timer que se encargara de crear la comida
        self.timer_crea_comida = QTimer(self)
        self.timer_crea_comida.setInterval(50)
        self.timer_crea_comida.timeout.connect(self.creador_de_comida)
        self.timer_crea_comida.start()

        self.comida = []

    def creador_de_comida(self):
        nueva_comida = Comida(self, self.width(), self.height())
        nueva_comida.actualizar.connect(self.actualizar_label)
        self.comida.append(nueva_comida)
        self.comida_creada += 1
        print(f"Has creado {self.comida_creada} unidades de comida\n")

    def actualizar_label(self, label, x, y):
        label.move(x, y)


if __name__ == '__main__':
    app = QApplication([])
    ex = MyWindow()
    app.exec_()
