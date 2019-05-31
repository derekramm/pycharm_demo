import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 5884)
server_socket.bind(address)
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    print(f'connect address: {addr}')

    msg = 'welcome to server'
    client_socket.send(msg.encode())
    client_socket.close()
