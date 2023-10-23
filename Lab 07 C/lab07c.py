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

response_parts = response.split(b"\r\n\r\n", 1)

http_headers = response_parts[0].decode('utf-8')
html_content = response_parts[1]

response_line = http_headers.split('\r\n', 1)[0]
response_code, response_message = response_line.split(' ', 1)

print("Response Code:", response_code)
print("Response Message:", response_message)

headers_dict = {}
headers_lines = http_headers.split('\r\n')[1:]  # Skip the first line (response line)
for header_line in headers_lines:
    key, value = header_line.split(':', 1)
    headers_dict[key.strip()] = value.strip()

print("\nHTTP Headers:")
for key, value in headers_dict.items():
    print(key + ":", value)

if response_code != '200':
    print("\nError: HTTP Response Code", response_code)
else:
    print("\nHTML Content:")
    print(html_content.decode('utf-8'))
