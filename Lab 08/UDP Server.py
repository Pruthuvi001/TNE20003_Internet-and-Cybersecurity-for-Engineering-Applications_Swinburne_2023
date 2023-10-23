import socket

server_host = '127.0.0.1'
server_port = 1025
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_host, server_port))
print(f"Server is listening on {server_host}:{server_port}")

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)  # Adjust buffer size if needed
        message = data.decode('utf-8')

        # Check if the message follows the protocol
        if message.startswith("TNE20003:"):
            _, _, client_message = message.partition(':')
            if len(client_message) > 0:
                response_message = f"TNE20003:A:{client_message}"
                server_socket.sendto(response_message.encode('utf-8'), client_address)
                print(f"Received from {client_address}: {client_message}")
            else:
                error_message = "Invalid message format"
                response_message = f"TNE20003:E:{error_message}"
                server_socket.sendto(response_message.encode('utf-8'), client_address)
                print(f"Error: {error_message}")
        else:
            error_message = "Invalid message format"
            response_message = f"TNE20003:E:{error_message}"
            server_socket.sendto(response_message.encode('utf-8'), client_address)
            print(f"Error: {error_message}")
    except KeyboardInterrupt:
        print("Server terminated by user")
        break
