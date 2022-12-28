import socket
import threading
from threading import *
import time

lock = threading.Lock()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7777))
print('Aguardando conexões.\n')
server.listen(2)

connection, address = server.accept()

while True:

    lock.acquire()

    value = connection.recv(1024).decode()
    value2 = connection.recv(1024).decode()

    def thread1():
        global num1
        num1 = int(value)
        time.sleep(0.1)

    def thread2():
        global num2
        num2 = int(value2)
        time.sleep(0.1)

    resultado = (num1 + num2)

    lock.release()

    Thread1 = Thread(target=thread1, args=())
    Thread2 = Thread(target=thread2, args=())

    Thread1.start()
    Thread2.start()

    res = str(resultado)
    connection.send(res.encode())
