import sys
import os
from threading import Thread
from time import sleep

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QGridLayout, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QCoreApplication, QRect, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap

# Ventana con eventos y señales

'''
class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.label1 = QLabel('Status:', self)
        self.grilla = QGridLayout()

        valores = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '0', 'CE', 'C']

        posiciones = [(i, j) for i in range(4) for j in range(3)]
        
        for posicion, valor in zip(posiciones, valores):
            boton = QPushButton(valor, self)

            """
            Aquí conectamos el evento clicked() de cada boton con el slot
            correspondiente. En este ejemplo todos los botones usan el
            mismo slot (self.boton_clickeado).
            """
            boton.clicked.connect(self.boton_clickeado)

            self.grilla.addWidget(boton, *posicion)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        self.move(300, 150)
        self.setWindowTitle('Calculator')

    def boton_clickeado(self):
        """
        Esta función se ejecuta cada vez que uno de los botones de la grilla
        es presionado. Cada vez que el botón genera el evento, la función inspecciona
        cual botón fue presionado y recupera la posición en que se encuentra en
        la grilla.
        """

        # Sender retorna el objeto que fue clickeado.
        # Ahora, la variable boton referencia una instancia de QPushButton
        boton = self.sender()

        # Obtenemos el identificador del elemento en la grilla
        idx = self.grilla.indexOf(boton)

        # Con el identificador obtenemos la posición del ítem en la grilla
        posicion = self.grilla.getItemPosition(idx)

        # Actualizamos label1
        self.label1.setText(f'Status: Presionado boton {idx}, en fila/columna: {posicion[:2]}.')


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec_())
'''

# Ventana con sender

'''
class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.label1 = QLabel('Status: -', self)

        """
        El evento de cada botón es conectado con su slot. En este caso es 
        el mismo método boton_callback().
        """
        self.boton1 = QPushButton('&Boton 1', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.clicked.connect(self.boton_clickeado)

        self.boton2 = QPushButton('&Boton 2', self)
        self.boton2.resize(self.boton2.sizeHint())
        self.boton2.clicked.connect(self.boton_clickeado)

        self.boton3 = QPushButton('&Salir', self)
        self.boton3.resize(self.boton3.sizeHint())
        self.boton3.clicked.connect(QCoreApplication.instance().quit)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.boton1)
        hbox.addWidget(self.boton2)
        hbox.addWidget(self.boton3)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.label1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)

        # Agregamos todos los elementos al formulario
        self.setGeometry(200, 100, 300, 200)
        self.setWindowTitle('Sender')

    def boton_clickeado(self):
        # Esta función registra el objeto que envía la señal del evento
        # y lo refleja mediante el método sender() en label3.
        sender = self.sender()
        self.label1.setText(f'Status: presionado botón {sender.text()}')
        self.label1.resize(self.label1.sizeHint())


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec_())
'''

# Ventana con Press Event

'''
class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(300, 100, 225, 450)
        self.setMaximumHeight(450)
        self.setMaximumWidth(225)
        self.setWindowTitle('mousePressEvent')

        self.mostrar_azul = True
        self.label_azul = QLabel('AZUL', self)
        self.label_azul.move(0, 0)
        self.label_azul.setGeometry(QRect(0, 0, 225, 225))  # (x, y, height, width)
        ruta_imagen_azul = os.path.join('Semana 9', 'img', 'colors', 'azul.png')
        self.pixmap_azul = QPixmap(ruta_imagen_azul)
        self.label_azul.setPixmap(self.pixmap_azul)
        self.label_azul.show()

        self.mostrar_verde = True
        self.label_verde = QLabel('VERDE', self)
        self.label_verde.move(0, 0)
        self.label_verde.setGeometry(QRect(0, 225, 225, 225))
        ruta_imagen_verde = os.path.join('Semana 9', 'img', 'colors', 'verde.png')
        self.pixmap_verde = QPixmap(ruta_imagen_verde)
        self.label_verde.setPixmap(self.pixmap_verde)
        self.label_verde.show()

        self.show()

    def mousePressEvent(self, event):
        if event.y() <= 225:  # Este es el alto del label
            if self.mostrar_azul:
                self.label_azul.hide()
            else:
                self.label_azul.show()
            self.mostrar_azul = not self.mostrar_azul
        else:
            if self.mostrar_verde:
                self.label_verde.hide()
            else:
                self.label_verde.show()
            self.mostrar_verde = not self.mostrar_verde


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())
'''

# Ventana Move Event

'''
class MiVentana(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(300, 100, 225, 450)
        self.setMaximumHeight(450)
        self.setMaximumWidth(225)
        self.setWindowTitle('Move Event')
        
        # Creamos el label
        self.label_azul = QLabel('AZUL', self)
        self.label_azul.move(0, 0)
        self.label_azul.setGeometry(QRect(0, 0, 225, 225))  # (x, y, height, width)
        
        self.label_verde = QLabel('VERDE', self)
        self.label_verde.move(0, 0)
        self.label_verde.setGeometry(QRect(0, 225, 225, 225))
        
        ruta_imagen_azul = os.path.join('Semana 9', 'img' ,'colors', 'azul.png')
        self.pixmap_azul = QPixmap(ruta_imagen_azul) # Creamos el pixmap
        ruta_imagen_verde = os.path.join('Semana 9', 'img' ,'colors', 'verde.png')
        self.pixmap_verde = QPixmap(ruta_imagen_verde)
        
        self.label_azul.setPixmap(self.pixmap_azul) # Asignamos el pixmap
        self.label_verde.setPixmap(self.pixmap_verde)
        
        self.setMouseTracking(True) # Activamos el tracking en nuestra ventana
        self.label_azul.setMouseTracking(True)
        self.label_azul.show()
        self.label_verde.show()
        self.show()

    def mouseMoveEvent(self, event):
        objeto_posicion = event.pos()
        print(objeto_posicion.x(), objeto_posicion.y()) 


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())
'''

# Ventana KBoard Event

'''
class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):
        self.etiqueta = QLabel('Etiqueta', self)
        self.etiqueta.move(20, 10)
        self.resize(self.etiqueta.sizeHint())

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Teclado')
        self.show()

    def keyPressEvent(self, event):
        """
        Este método maneja el evento que se produce al presionar las teclas.
        """
        self.etiqueta.setText(f'Presionaron la tecla: {event.text()} de código: {event.key()}')
        self.etiqueta.resize(self.etiqueta.sizeHint())


if __name__ == '__main__':
    app = QApplication([])
    ex = MiVentana()
    sys.exit(app.exec_())
'''

# Señales Personalizadas

'''
class MiSenal(QObject):
    """
    Esta clase contiene la señal que permite la comunicación entre
    elementos de la GUI.
    """
    senal = pyqtSignal()


class VentanaPresionable(QWidget):

    def __init__(self, senal_escribir):
        super().__init__()

        self.senal_escribir = senal_escribir

        self.inicializa_gui()

    def inicializa_gui(self):
        self.etiqueta = QLabel('Presiona esta ventana', self)
        self.etiqueta.move(20, 10)
        self.etiqueta.resize(self.etiqueta.sizeHint())

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emite señal')
        self.show()

    def mousePressEvent(self, event):
        # Al ejecutar la siguiente línea, se emite la señal,
        # y los métodos conectados se llamarán automáticamente.
        self.senal_escribir.emit()


class VentanaQueSeEdita(QWidget):

    def __init__(self, senal_editar):
        super().__init__()

        self.senal_editar = senal_editar
        # Conectamos el método encargado de ejecutar la tarea
        self.senal_editar.connect(self.edita_etiqueta)

        self.inicializa_gui()

    def inicializa_gui(self):

        self.etiqueta = QLabel('', self)
        self.etiqueta.move(20, 10)
        self.etiqueta.resize(self.etiqueta.sizeHint())

        self.setGeometry(700, 300, 290, 150)
        self.setWindowTitle('Recibe señal')
        self.show()

    def edita_etiqueta(self):
        self.etiqueta.setText('¡Oh! Alguien ha presionado el mouse')
        self.etiqueta.resize(self.etiqueta.sizeHint())


if __name__ == '__main__':
    app = QApplication([])
    senal = MiSenal()
    ventana_1 = VentanaPresionable(senal.senal)
    ventana_2 = VentanaQueSeEdita(senal.senal)
    sys.exit(app.exec_())
'''

# Emision de eventos con información

'''
class MisSenales(QObject):
    """
    Esta clase contiene las señales que permite la comunicación entre
    elementos de la GUI.
    """
    senal_simple = pyqtSignal() # Señal simple
    senal_texto = pyqtSignal(str) # Señal que permite enviar texto
    senal_coordenadas = pyqtSignal(int, int) # Señal que permite enviar dos ints


class VentanaPresionable(QWidget):

    def __init__(self, senal_simple, senal_texto, senal_coor):
        super().__init__()
        # Se guarda referencia a todas las señales que puede emitir esta ventana
        self.senal_simple = senal_simple
        self.senal_texto = senal_texto
        self.senal_coor = senal_coor

        self.inicializa_gui()

    def inicializa_gui(self):
        self.etiqueta = QLabel('Texto etiqueta', self)
        self.etiqueta.move(20, 10)
        self.etiqueta.resize(self.etiqueta.sizeHint())

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emite señal')
        self.setMouseTracking(True)
        self.show()

    def mousePressEvent(self, event):
        # Se emite la señal simple, sin argumento
        self.senal_simple.emit()
        # Se emite la señal que permite envir un str
        # Se envia el contenido de la etiqueta de la ventana
        self.senal_texto.emit(self.etiqueta.text())

    def mouseMoveEvent(self, event):
        # Se emite la señal que permite enviar dos ints, enviamos la posición del mouse
        self.senal_coor.emit(event.pos().x(), event.pos().y())


class VentanaQueSeEdita(QWidget):

    def __init__(self, senal_simple, senal_texto, senal_coor):
        super().__init__()

        self.senal_simple = senal_simple
        self.senal_texto = senal_texto
        self.senal_coor = senal_coor
        # Conectamos los métodos de respuesta de cada señal
        self.senal_simple.connect(self.edita_etiqueta_1)
        self.senal_texto.connect(self.edita_etiqueta_2)
        self.senal_coor.connect(self.edita_etiqueta_3)

        self.inicializa_gui()

    def inicializa_gui(self):

        self.etiqueta_1 = QLabel('', self)
        self.etiqueta_1.move(20, 10)
        self.etiqueta_1.resize(self.etiqueta_1.sizeHint())

        self.etiqueta_2 = QLabel('', self)
        self.etiqueta_2.move(20, 40)
        self.etiqueta_2.resize(self.etiqueta_2.sizeHint())

        self.etiqueta_3 = QLabel('', self)
        self.etiqueta_3.move(20, 70)
        self.etiqueta_3.resize(self.etiqueta_3.sizeHint())

        self.setGeometry(700, 300, 290, 150)
        self.setWindowTitle('Recibe señal')
        self.show()
    
    def edita_etiqueta_1(self):
        # Este método no tiene argumentos, ya que es una señal simple
        self.etiqueta_1.setText('¡Oh! Alguien ha presionado el mouse')
        self.etiqueta_1.resize(self.etiqueta_1.sizeHint())

    def edita_etiqueta_2(self, texto):
        # Este método tiene un argumento, el str que se espera del evento conectado
        self.etiqueta_2.setText(f'Recibí del evento: {texto}')
        self.etiqueta_2.resize(self.etiqueta_2.sizeHint())

    def edita_etiqueta_3(self, x, y):
        # Este método tiene dos argumentos, los ints que se espera del evento conectado
        self.etiqueta_3.setText(f'Recibí posiciones: {x}, {y}')
        self.etiqueta_3.resize(self.etiqueta_3.sizeHint())


if __name__ == '__main__':
    app = QApplication([])
    senales = MisSenales()
    ventana_1 = VentanaPresionable(senales.senal_simple, senales.senal_texto, senales.senal_coordenadas)
    ventana_2 = VentanaQueSeEdita(senales.senal_simple, senales.senal_texto, senales.senal_coordenadas)
    sys.exit(app.exec_())
'''

# Señales personalizadas y threads

'''
class MiThread(Thread):
    """
    Esta clase representa un thread personalizado que será utilizado durante
    la ejecución de la GUI.
    """

    def __init__(self, senal_actualizar, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.senal_actualizar = senal_actualizar

    def run(self):
        for i in range(10):
            sleep(0.5)
            self.senal_actualizar.emit(str(i))

        sleep(0.5)
        self.senal_actualizar.emit('Status: thread terminado')


class MiVentana(QWidget):

    # Creamos una señal para manejar la respuesta del thread
    senal_thread = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.thread = None
        # Conectamos la señal del thread al método que maneja
        self.senal_thread.connect(self.actualizar_labels)

        self.init_gui()

    def init_gui(self):
        # Configuramos los widgets de la interfaz
        self.label = QLabel('Status: esperando thread', self)
        self.boton = QPushButton('Ejecutar Thread', self)
        self.boton.clicked.connect(self.ejecutar_threads)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.boton)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        self.setLayout(vbox)

        # Configuramos las propiedades de la ventana.
        self.setWindowTitle('Ejemplo threads')
        self.setGeometry(50, 50, 250, 200)
        self.show()

    def ejecutar_threads(self):
        """
        Este método crea un thread cada vez que se presiona el botón en la
        interfaz. El thread recibirá como argumento la señal sobre la cual
        debe operar.
        """
        if self.thread is None or not self.thread.is_alive():
            self.thread = MiThread(self.senal_thread)
            self.thread.start()

    def actualizar_labels(self, evento):
        """
        Este método actualiza el label según los datos enviados desde el
        thread através del objeto evento. Para este ejemplo, el método
        recibe el evento, pero podría también no recibir nada.
        """
        self.label.setText(evento)


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())
'''