import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1",9000))

server_socket.listen(1)

print("Waiting for connection")

conn,addr = server_socket.accept()

data = conn.recv(1024).decode()

print("Message from Client:",data)

conn.send("message received:".encode())

conn.close()

server_socket.close()