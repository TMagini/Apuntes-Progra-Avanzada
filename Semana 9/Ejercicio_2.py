import sys
import os
from threading import Thread
from time import sleep

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QGridLayout, QVBoxLayout, QHBoxLayout,
                             QRadioButton, QSpinBox, QCheckBox)
from PyQt5.QtCore import QCoreApplication, QRect, QObject, pyqtSignal
from PyQt5.QtGui import QPixmap

class Formulario(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):

        self.setWindowTitle("Formulario")
        self.setGeometry(200, 200, 400, 400)

        self.etiqueta_1 = QLabel("Usuario", self)
        self.etiqueta_2 = QLabel("Género", self)
        self.etiqueta_3 = QLabel("Edad", self)
        self.etiqueta_4 = QLabel("Configuración", self)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(QRadioButton('Femenino'))
        vbox1.addWidget(QRadioButton('Masculino'))
        vbox1.addWidget(QRadioButton('No Binario'))
        vbox1.addWidget(QRadioButton('No mencionar'))

        spin = QSpinBox()
        spin.setMinimum(18)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(QCheckBox('Cuenta Privada'))
        vbox2.addWidget(QCheckBox('Recibir Noticias'))
        vbox2.addWidget(QCheckBox('Acepto términos y condiciones'))

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.etiqueta_1)
        hbox1.addWidget(QLineEdit('', self))
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.etiqueta_2)
        hbox2.addLayout(vbox1)
        hbox2.addStretch(1)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.etiqueta_3)
        hbox3.addWidget(spin)
        hbox3.addStretch(1)

        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(self.etiqueta_4)
        hbox4.addLayout(vbox2)
        hbox4.addStretch(1)


        # Crea contenedor vertical para colocar los campos
        contenedor = QVBoxLayout()

        contenedor.addLayout(hbox1)
        contenedor.addLayout(hbox2)
        contenedor.addLayout(hbox3)
        contenedor.addLayout(hbox4)
        contenedor.addWidget(QPushButton('Continuar'))
        
        # Fijamos el Layout completo
        self.setLayout(contenedor)
        
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    formulario = Formulario()
    sys.exit(app.exec())