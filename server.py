import socket

HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode("utf-8")

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

isActive = False
for i in range(0, 256):
    if isActive == True:
        i -= 1
        break
    for j in range(0, 256):
        try:
            socket_server.bind((f"192.168.{i}.{j}", 12345))
            isActive = True
            break
        except:
            pass
socket_server.listen(1)
print(f"192.168.{i}.{j}\nlistening")

socket_client, address_client = socket_server.accept()
print("connected:", address_client)

data = socket_client.recv(1024).decode("utf-8")
print(data)

content = HDRS + data.encode("utf-8")

socket_client.send(content)

socket_client.close()
#socket_server.close()
