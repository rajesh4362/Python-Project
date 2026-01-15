import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345

server.bind((host, port))
server.listen(1)

print("Server started...")
conn, addr = server.accept()
print("Client connected:", addr)

while True:
    message = conn.recv(1024).decode()
    if message.lower() == "exit":
        print("Client disconnected.")
        break

    print("Client:", message)
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()
server.close()
