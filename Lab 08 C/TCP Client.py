import socket

server_host = '127.0.0.1'
server_port = 1025
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

messages = ["Hello, server!", "Another message"]
for message in messages:
    formatted_message = f"TNE20003:{message}\n"
    client_socket.send(formatted_message.encode('utf-8'))
    print(f"Sent to {server_host}:{server_port}: {message}")

client_socket.close()

