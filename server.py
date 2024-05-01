import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind('localhost', 12345)
socket_server.listen(1)
print("listening")

socket_client, address_client = socket_server.accept()
print("connected:", address_client_client)

data = socket_client.recv(1024)
print(data)

connect.send(data.upper())

connect.close()
sock.close()