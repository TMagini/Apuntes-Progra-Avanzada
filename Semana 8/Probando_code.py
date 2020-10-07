import threading
import time


class CuentaOvejas(threading.Thread): # Hereda de Thread
    """Este será nuestro nuevo Cuenta Ovejas basado en Thread"""
    def __init__(self, nombre, max_ovejas):
        # En el caso de los threads, lo primero es invocar al init original. SIEMPRE.
        super().__init__(name=nombre)
        self.max_ovejas = max_ovejas # Se agrega un atributo de instancia extra
    
    def run(self):
        # Este metodo define las instrucciones a ejecutar de este thread
        # cuando lo ejecutamos el metodo start()
        print(f"{self.name} tiene sueño...")
        tiempo_partida = time.time()
        for numero in range(1, self.max_ovejas + 1):
            time.sleep(1)
            print(f"({self.name}: {numero} oveja{'s' if numero > 1 else ''})")
        print(f"{self.name} a dormir...")
        print(f"{self.name} se durmió después de {time.time() - tiempo_partida} seg.")

        
class CuentaLiebres(threading.Thread): # Hereda de Thread
    """
    Este será un nuevo Cuenta Liebres basado en Thread
    Las liebres son más rápidas, así que cuenta dos por segundo
    """
    def __init__(self, nombre, max_liebres):
        super().__init__(name=nombre)
        self.max_liebres = max_liebres
    
    def run(self):
        print(f"{self.name} tiene sueño...")
        tiempo_partida = time.time()
        for numero in range(1, self.max_liebres + 1):
            if numero % 2 == 1:
                time.sleep(1)
            print(f"({self.name}: {numero} liebre{'s' if numero > 1 else ''})")
        print(f"{self.name} a dormir...")
        print(f"{self.name} se durmió después de {time.time() - tiempo_partida} seg.")

# Usamos la definicion de los Thread declarados en el ejemplo anterior
# Se crean los threads usando la clase Thread.
cristian = CuentaOvejas("Cristian", 3)
cot = CuentaOvejas("Cote", 6)
antonio = CuentaLiebres("Antonio", 3)
joaquin = CuentaLiebres("Joaquin", 15)

# Se inicializan los threads creados
cristian.start()
cot.start()
antonio.start()
joaquin.start()
print("Ayudantes: Los profes se fueron a la cama...")

antonio.join()  # Esperaremos lo que sea necesario.
print("Ayudantes: ¡ANTONIO SE DURMIÓ!")
cristian.join() # No especificamos timeout, esperará lo que sea necesario
print("Ayudantes: ¡CRISTIAN SE DURMIÓ!")
cot.join() # Esperaremos lo que sea necesario.
print("Ayudantes: ¡COTE SE DURMIÓ!")
joaquin.join(1)  # Esperaremos máximo 1 segundos después del último dormido, ya es muy tarde

if joaquin.is_alive():
    print("Ayudantes: Vicente sigue despierto 😞. A la casa cabros.")
else:
    print("Ayudantes: ¡Todos los profes se durmieron! ¡A festejar!")
    for i in range(10):
        print("Ayudantes: 🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶🎵🎶")
        time.sleep(1)

'''
import threading

def contar_diez_ovejas():
    print("Tengo sueño...")
    for numero in range(1, 11):
        print(f"({numero} oveja{'s' if numero > 1 else ''})")
    print("A dormir...")


mi_hilo = threading.Thread(target=contar_diez_ovejas)

mi_hilo.start()
'''