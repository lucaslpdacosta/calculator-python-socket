import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print('Cliente conectado.')

while True:

    n1 = ''
    n2 = ''

    while not (n1.isnumeric()):
        n1 = input('\ninforme o primeiro numero: ')
        client.send(n1.encode())
        if not (n1.isnumeric()):
            print('valor invalido, tente novamente.\n')

    while not (n2.isnumeric()):
        n2 = input('informe o segundo numero: ')
        client.send(n2.encode())
        if not (n2.isnumeric()):
            print('valor invalido, tente novamente.\n')

    result = client.recv(1024)

    print('\nresultado:  {} + {} = {}' .format(n1, n2, result.decode()))

    opt = input('\npressione 1 para continuar ou qualquer tecla para sair: ')
    if opt == '1':
        continue
    else:
        print('fechando conexao')
        break

client.close()
