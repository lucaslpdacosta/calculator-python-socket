import socket
import threading
from threading import *

lock = threading.Lock()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7777))
print('Aguardando conexões.\n')
server.listen(2)

connection, address = server.accept()

while True:

    lock.acquire()

    input = connection.recv(1024)
    value = input.decode()

    input2 = connection.recv(1024)
    value2 = input2.decode()

    num1 = int(value)
    num2 = int(value2)

    resultado = (num1 + num2)

    lock.release()

    res = str(resultado)
    connection.send(res.encode())

    connection.close
