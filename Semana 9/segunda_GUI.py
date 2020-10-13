import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtGui import QPixmap

# Ventanas con texto y etiquetas

'''
class MiVentana(QWidget):

    def __init__(self, *args, **kwargs):
        """
        Este método inicializa la ventana.
        """
        super().__init__(*args, **kwargs)
        
        # Llamamos a un método propio que inicializa los elementos de la ventana
        self.init_gui()

    def init_gui(self):
        """
        Este método configura la interfaz y todos sus widgets,
        posterior a __init__().
        """
        # Ajustamos la geometría de la ventana y su título
        self.setGeometry(200, 100, 200, 300)
        self.setWindowTitle('Ventana con label y cuadro de texto')
        
        # Agregamos etiquetas usando el widget QLabel(texto_inicial, padre)
        self.label1 = QLabel('Texto:', self)
        self.label1.move(10, 15)

        self.label2 = QLabel('Esta etiqueta es variable', self)
        self.label2.move(10, 50)

        # Agregamos cuadros de texto mediante QLineEdit(texto_inicial, padre)
        self.edit = QLineEdit('', self)
        self.edit.setGeometry(45, 15, 100, 20)

        # Una vez que fueron agregados todos los elementos a la ventana la
        # desplegamos en pantalla
        self.show()


if __name__ == '__main__':
    """
    Recordar que en el programa principal debe existir una instancia de
    QApplication ANTES de crear los demas widgets, incluida la ventana
    principal.
    Si la aplicación no recibe parámetros desde la línea de comandos,
    QApplication recibe una lista vacia como QApplication([]).
    """

    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())
'''

# Ventanas con imagenes

'''
class MiVentana(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Este método inicializa la interfaz y todos sus widgets.
        """
        
        # Ajustamos la geometría de la ventana y su título
        self.setGeometry(200, 100, 200, 200)
        self.setWindowTitle('Ventana con imagen')
        
        
        # Creamos el QLabel que contendrá la imagen y definimos su tamaño
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 100, 100)
        
        # Escribimos la ruta al archivo que contiene la imagen.
        # La imagen obtenida en https://en.wikipedia.org/wiki/Python_(genus)
        ruta_imagen = os.path.join('Semana 9','img', 'python.jpg')
        
        # Cargamos la imagen como pixeles 
        pixeles = QPixmap(ruta_imagen)
        
        # Agregamos los pixeles al elemento QLabel
        self.label.setPixmap(pixeles)
        
        # Finalmente, ajustamos tamaño de contenido al tamaño del elemento (100 x 100)
        self.label.setScaledContents(True)
        
        
        # Una vez que fueron agregados
        # todos los elementos a la ventana la
        # desplegamos en pantalla
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec_())
'''

# Ventana con botones

'''
class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Este método inicializa la interfaz y todos sus widgets.
        """
        
        # Ajustamos la geometria de la ventana
        self.setGeometry(200, 100, 200, 300)
        self.setWindowTitle('Ventana con botón')

        # Podemos agrupar conjuntos de widgets en alguna estructura
        self.labels = {}
        self.labels['label1'] = QLabel('Texto:', self)
        self.labels['label1'].move(10, 15)
        self.labels['label2'] = QLabel('Aquí se escribe la respuesta', self)
        self.labels['label2'].move(10, 50)

        self.edit1 = QLineEdit('', self)
        self.edit1.setGeometry(45, 15, 100, 20)

        """
        El uso del caracter & al inicio del texto de algún botón o menú permite
        que la primera letra del mensaje mostrado esté destacada. La
        visualización depende de la plataforma utilizada.
        El método sizeHint provee un tamaño sugerido para el botón.        
        """
        self.boton1 = QPushButton('&Procesar', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(5, 70)
        
        # Una vez que fueron agregados todos los elementos a la ventana la
        # desplegamos en pantalla
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())
'''

# Ventanas con layouts

'''
class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Este método configura todos los widgets de la ventana.
        """
        self.setGeometry(100, 100, 300, 300)
        self.label1 = QLabel('Texto:', self)
        self.edit1 = QLineEdit('', self)
        self.edit1.resize(100, 20)
        self.boton1 = QPushButton('&Calcular', self)
        self.boton1.resize(self.boton1.sizeHint())

        """
        Creamos el layout horizontal y agregamos los widgets mediante el
        método addWidget(). El método addStretch() nos permite incluir
        opcionalmente espaciadores.
        """
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label1)
        hbox.addWidget(self.edit1)
        hbox.addWidget(self.boton1)
        hbox.addStretch(1)

        """
        Creamos el layout vertical y le agregamos el layout horizontal.
        Opcionalmente agregamos espaciadores para distribuir los widgets.
        Notar el juego entre el valor recibido por los espaciadores.
        """

        vbox = QVBoxLayout()
        vbox.addStretch(5)
        vbox.addLayout(hbox)
        vbox.addStretch(5)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec_())

'''

# Ventanas con Grid Layout

'''
class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):

        # Creamos una etiqueta para status. Recordar que los widgets simples
        # no tienen StatusBar.
        self.label = QLabel('Status:', self)

        # Creamos la grilla para ubicar los widgets de manera matricial
        self.grilla = QGridLayout()

        valores = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '0', 'CE', 'C']

        # Generamos las posiciones de los botones en la grilla y le asociamos
        # el texto que debe desplegar cada botón guardados en la lista valores
        posiciones = [(i, j) for i in range(4) for j in range(3)]
        
        for posicion, valor in zip(posiciones, valores):
            boton = QPushButton(valor, self)
            self.grilla.addWidget(boton, *posicion)

        # Creamos un layout vertical
        vbox = QVBoxLayout()

        # Agregamos el label al layout con addWidget
        vbox.addWidget(self.label)

        # Agregamos el layout de la grilla al layout vertical con addLayout
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        self.move(300, 150)
        self.setWindowTitle('Calculator')


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    form.show()
    sys.exit(app.exec_())
'''

# Ventana con POO

'''
class MiBoton(QPushButton):
    
    # Recibe dos argumentos extra además de los regulares de QPushButton
    # Un nombre para identificar el botón
    # Una posición para ubicarse en la ventana
    def __init__(self, nombre, pos, *args, **kwargs):
        # Llama al constructor de la clase madre
        super().__init__(*args, **kwargs)
        
        # Asigna el nombre a la instancia
        self.nombre = nombre
        
        # Crea un contador de instancia inicialmente en 0
        self.contador = 0
        
        # Fija su propia geometría
        self.resize(self.sizeHint())
        self.move(*pos)
        
        # La siguiente línea conecta un clic con el método contar
        # Entenderemos mejor esta línea en el siguiente notebook
        self.clicked.connect(self.contar)
        
    # Agregamos comportamiento al botón, aumenta el contador en cada clic
    def contar(self):
        self.contador += 1
        print(f'{self.nombre} apretado {self.contador} veces.')


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        # Fija la geometría de la ventana principal
        self.setGeometry(200, 200, 100, 100)
        self.setMaximumHeight(100)
        self.setMaximumWidth(100)
        
        # Instancia dos botones de nuestra clase, con atributos extra
        # de los que QPushButton está acostumbrado: nombre y posición
        self.boton_1 = MiBoton('Botón 1', (23, 20), 'Aprétame', self)
        self.boton_2 = MiBoton('Botón 2', (23, 60), 'Aprétame', self)
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec_())
'''

# Ventana ejemplo de formulario

class CampoFormulario(QHBoxLayout):
    # Heredamos de Layout Horizontal para colocar cada campo.

    def __init__(self, texto, *args, **kwargs):
        # Llama al constructor de la clase madre
        super().__init__(*args, **kwargs)
        
        # Crea la etiqueta y cuadro correspondientes
        label = QLabel(f"{texto}: ")
        campo = QLineEdit("")
        
        # Los coloca dentro del Layout
        self.addStretch(1)
        self.addWidget(label)
        self.addWidget(campo)
        self.addStretch(1)

class Formulario(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Fija datos de ventana
        self.setWindowTitle("Formulario")
        self.setGeometry(200, 200, 400, 400)
        
        # Crea contenedor vertical para colocar los campos
        contenedor = QVBoxLayout()
        
        # Coloca cada campo que creamos
        contenedor.addLayout(CampoFormulario("Nombre"))
        contenedor.addLayout(CampoFormulario("Apellido"))
        contenedor.addLayout(CampoFormulario("Dirección"))
        contenedor.addLayout(CampoFormulario("Correo"))
        contenedor.addLayout(CampoFormulario("Usuario"))
        contenedor.addLayout(CampoFormulario("Contraseña"))
        
        # Fijamos el Layout completo
        self.setLayout(contenedor)
        
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    formulario = Formulario()
    sys.exit(app.exec())