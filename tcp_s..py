import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socKettt:
    socKettt.bind(('127.0.0.1',50007))
    socKettt.listen(1)
    while True:
        connection, fromaddr = socKettt.accept()
        with connection:
            while True:
                receivedata = connection.recv(1024)
                if not receivedata:
                    break
                print('data : {}, addr: {}'.format(receivedata, fromaddr))
                #connECtion.sendall(b'received')
