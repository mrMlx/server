import socket

HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode("utf-8")

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

localIP = "192.168.0.54"
port = 12345
socket_server.bind((localIP, port)) # your ip and port
print(f"local IP {localIP} "
      f"port {port}")

socket_server.listen(4)
print("listening")

socket_client, address_client = socket_server.accept()
print("connected:", address_client)

data = socket_client.recv(1024).decode("utf-8")
print(data)

content = HDRS + data.encode("utf-8")

socket_client.send(content)

socket_client.close()
socket_server.close()
