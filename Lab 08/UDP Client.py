import socket

server_host = '127.0.0.1'
server_port = 1025
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

messages = ["Hello, server!", "Another message"]
for message in messages:
    formatted_message = f"TNE20003:{message}"
    client_socket.sendto(formatted_message.encode('utf-8'), (server_host, server_port))
    print(f"Sent to {server_host}:{server_port}: {message}")

while True:
    try:
        response_data, server_address = client_socket.recvfrom(1025)  # Adjust buffer size if needed
        response_message = response_data.decode('utf-8')

        if response_message.startswith("TNE20003:A:"):
            _, _, server_response = response_message.partition(':')
            print(f"Received from server: {server_response}")
        elif response_message.startswith("TNE20003:E:"):
            _, _, error_message = response_message.partition(':')
            print(f"Server Error: {error_message}")
        else:
            print(f"Invalid response from server: {response_message}")
    except KeyboardInterrupt:
        print("Client terminated by user")
        break
