import socket

host = 'www.google.com'
port = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

request = "GET / HTTP/1.0\r\nHost: {}\r\n\r\n".format(host)

client_socket.send(request.encode())

response = b""

while True:
    data = client_socket.recv(4096)
    if not data:
        break
    response += data

client_socket.close()

print(response.decode('utf-8'))
