import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sOcKettt:
    sOcKettt.bind(('127.0.0.1',50007))
    sOcKettt.listen(1)
    while True:
        connECtion, FROMaddr = sOcKettt.accept()
        with connECtion:
            while True:
                ReceiveData = connECtion.recv(1024)
                if not ReceiveData:
                    break
                print('data : {}, addr: {}'.format(ReceiveData, FROMaddr))
                #connECtion.sendall(b'received')
