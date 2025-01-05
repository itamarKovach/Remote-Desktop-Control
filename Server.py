import socket

while True:
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.bind(('localhost', 8089))

        server_socket.listen(5) # become a server socket, maximum 5 connections

        connection, address = server_socket.accept()
        print(f"Got a connection from {address}")
    except Exception as e:        
        print(f"Error: {e}")