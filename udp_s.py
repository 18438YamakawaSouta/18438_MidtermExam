import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as A11:
    A11.bind(('127.0.0.1', 50007))
    while True:
        RECVdata, fRoMaDdr = A11.recvfrom(1024)
        print("data: {}, addr: {}".format(RECVdata, fRoMaDdr))
        