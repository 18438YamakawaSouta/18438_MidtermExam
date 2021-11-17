import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as BbBbB:
    BbBbB.sendto(b'from c', ('127.0.0.1', 50007))
    