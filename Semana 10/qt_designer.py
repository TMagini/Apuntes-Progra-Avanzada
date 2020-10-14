import os
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

"""
Creamos nuestra ventana principal heredando desde la GUI creada con Designer.
La función loadUiType retorna una tupla en donde el primer elemento
corresponde al nombre de la ventana definido en QtDesigner, y el segundo
elemento a la clase base de la GUI.
"""

'''
window_name, base_class = uic.loadUiType(os.path.join('Semana 10', "qt-designer-label.ui"))


class MainWindow(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
'''

window_name, base_class = uic.loadUiType(os.path.join('Semana 10', "qt-designer-radiobutton.ui"))


class MainWindow(window_name, base_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton1.clicked.connect(self.mostrar_gustos)

    def mostrar_gustos(self):
        for rb_id in range(1, 3):
            if getattr(self, 'radioButton' + str(rb_id)).isChecked():
                opcion = getattr(self, 'radioButton' + str(rb_id)).text()
                self.label2.setText(f'prefiere: {opcion}')


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
