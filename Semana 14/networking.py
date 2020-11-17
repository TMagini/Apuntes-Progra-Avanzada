import socket

## Esta celda puede ser ejecutada desde aquí sin problemas.

'''sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "iic2333.ing.puc.cl"
port = 80

try:
    sock.connect((host, port))
    sock.sendall('GET / HTTP/1.1\nHost: iic2333.ing.puc.cl\n\n'.encode('utf-8'))
    data = sock.recv(4096)
    print(data.decode('utf-8'))
except ConnectionError as e:
    # ConnectionError es la clase base BrokenPipeError, ConnectionAbortedError,
    # ConnectionRefusedError y ConnectionResetError.
    print("Ocurrió un error.")
finally:
    # ¡No olvidemos cerrar la conexión!
    sock.close()'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Así podemos obtener el hostname de la máquina actual
host = socket.gethostname()
port = 9000

sock.bind((host, port))
sock.listen()

counter = 0
while counter < 5:
    try:
        socket_cliente, address = sock.accept()
        print("Conexión aceptada desde", address)
        socket_cliente.sendall("Gracias por conectarte\n".encode("utf-8"))
        socket_cliente.close()
        counter += 1
    except ConnectionError:
        print("Ocurrió un error.")

sock.close()


