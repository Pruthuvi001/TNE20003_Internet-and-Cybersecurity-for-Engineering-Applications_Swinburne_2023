import socket
import threading

server_host = '127.0.0.1'
server_port = 1025
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(5)  # Allow up to 5 simultaneous client connections

print(f"TCP Server is listening on {server_host}:{server_port}")

def handle_client(client_socket):
    try:
        data = b""
        while True:
            chunk = client_socket.recv(1025)  # Adjust buffer size as needed
            if not chunk:
                break
            data += chunk
            # Check for message termination (e.g., "\n" or custom delimiter)
            if b"\n" in data:
                messages = data.split(b"\n")
                for message in messages:
                    process_message(message.decode('utf-8'), client_socket)
                data = b""
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def process_message(message, client_socket):
    # Implement message processing logic here
    if message.startswith("TNE20003:"):
        _, _, client_message = message.partition(':')
        if len(client_message) > 0:
            response_message = f"TNE20003:A:{client_message}"
            client_socket.send(response_message.encode('utf-8'))
            print(f"Received from {client_socket.getpeername()}: {client_message}")
        else:
            error_message = "Invalid message format"
            response_message = f"TNE20003:E:{error_message}"
            client_socket.send(response_message.encode('utf-8'))
            print(f"Error: {error_message}")
    else:
        error_message = "Invalid message format"
        response_message = f"TNE20003:E:{error_message}"
        client_socket.send(response_message.encode('utf-8'))
        print(f"Error: {error_message}")

while True:
    try:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
    except KeyboardInterrupt:
        print("Server terminated by user")
        break

