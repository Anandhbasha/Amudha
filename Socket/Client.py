import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1",9000))

client_socket.send("Hello Server".encode())

# receive data from server

data = client_socket.recv(1024).decode()

# first run the server next run the client file

print("server says:",data)

client_socket.close()