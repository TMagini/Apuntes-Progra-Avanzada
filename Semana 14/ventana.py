import socket

'''sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtenemos el nombre de la máquina a la que nos queremos conectar.
# En este caso, nos queremos conectar a esta misma máquina.
host = socket.gethostname()
port = 9000

try:
    sock.connect((host, port))
    data = sock.recv(4096)
    print(data.decode("utf-8"))
except ConnectionError as e:
    print("[Cliente] Ocurrió un error")
finally:
    sock.close()'''