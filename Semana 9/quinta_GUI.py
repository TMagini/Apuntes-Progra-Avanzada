import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal

# Prueba con error

'''
class Ventana(QWidget):
    def __init__(self, titulo, x, y):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(x, y, 200, 50)
        self.boton = QPushButton("Abrir otra ventana", self)
        self.boton.clicked.connect(self.abrir_otra_ventana)

    def abrir_otra_ventana(self):
        self.hide() # Esconder la ventana actual
        otra_ventana = Ventana("Otra ventana", 300, 100) # Crear otra
        otra_ventana.show() # Mostrar nueva ventana


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana("Inicial", 100, 100)
    ventana.show()
    sys.exit(app.exec_())
'''

# Version sin error

'''
class Ventana(QWidget):
    def __init__(self, titulo, x, y):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(x, y, 200, 50)
        self.boton = QPushButton("Abrir otra ventana", self)
        self.boton.clicked.connect(self.abrir_otra_ventana)

    def abrir_otra_ventana(self):
        self.hide()
        self.otra_ventana = Ventana("Otra ventana", 300, 100)
        self.otra_ventana.show()


if __name__ == '__main__':
    app = QApplication([])
    ventana = Ventana("Inicial", 100, 100)
    ventana.show()
    sys.exit(app.exec_())
'''

# Arreglado el problema con señales

class Ventana(QWidget):
    
    # Cada ventana se instancia con una señal para ser abierta
    senal_abrir_ventana = pyqtSignal()
    
    def __init__(self, titulo, x, y):
        super().__init__()
        # Definimos lo básico de la ventana
        self.setWindowTitle(titulo)
        self.setGeometry(x, y, 200, 50)
        
        # La señal que le permite a esta ventana abrirse, 
        # se conecta a su propio show. Así, si alguien
        # emite la señal, esta ventana se mostrará
        self.senal_abrir_ventana.connect(self.show)
        
        # Definimos el atributo de instancia que contendría una
        # señal para abrir otra ventana, comienza como None
        self.senal_abrir_otra_ventana = None
        
        # Creamos botón que se conecta a método self.abrir_otra_ventana
        self.boton = QPushButton("Abrir otra ventana", self)
        self.boton.clicked.connect(self.abrir_otra_ventana)

    def abrir_otra_ventana(self):
        # Si tenemos una señal asociada para abrir otra ventana
        if self.senal_abrir_otra_ventana:
            # Ocultamos esta ventana y emitimos la señal para abrir otra
            self.hide()
            self.senal_abrir_otra_ventana.emit()


if __name__ == '__main__':
    app = QApplication([])
    
    # Instanciamos dos ventanas distintas
    # Cada una comienza con una señal propia que
    # le permite ser abierta por otra.
    ventana_1 = Ventana("Inicial", 100, 100)
    ventana_2 = Ventana("Alternativa", 500, 100)
    
    # Conectamos las señales correspondientes:
    # ventana 1 tiene acceso a la señal de ventana 2
    # Ahora ventana 2 puede ser abierta desde ventana 1
    ventana_1.senal_abrir_otra_ventana = ventana_2.senal_abrir_ventana
    
    # Con esta también vinculamos a ventana 1 desde ventana 2
    ventana_2.senal_abrir_otra_ventana = ventana_1.senal_abrir_ventana
    
    ventana_1.show()
    sys.exit(app.exec_())