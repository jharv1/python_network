#Test with $ nc -l 127.0.0.1 9999

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect(("127.0.0.1", 9999))

socket.send(b"Hello\n")

socket.close()