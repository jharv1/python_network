#Test with $ nc -l 127.0.0.1 9999

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(("127.0.0.1", 9999))

while 1:
    data = socket.recv(16)
    if not data:
        break
    print("data is ", data)

socket.close()