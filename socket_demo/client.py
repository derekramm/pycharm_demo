import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 5884)
s.connect(address)

msg = s.recv(1024)
s.close()

print(msg.decode())
