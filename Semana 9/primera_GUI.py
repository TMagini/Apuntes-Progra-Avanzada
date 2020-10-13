import sys
from PyQt5.QtWidgets import QWidget, QApplication

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(200, 100, 300, 300)

        # Podemos dar nombre a la ventana (Opcional)
        self.setWindowTitle('Mi Primera Ventana')


if __name__ == '__main__':

    # Esta funcion imprime (en la mayoria de los casos) el error que hace caer el programa

    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())