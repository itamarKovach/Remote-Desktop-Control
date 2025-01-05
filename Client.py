import socket
from pynput import keyboard

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8089))

count = 0

while count != 5:

    count += 1

    special = client_socket.recv(1).decode()
    print(special)
    key_to_press = None
    if(special == 'y'):
        key_to_press = client_socket.recv(3).decode()
        keyboard.Controller().press(key_to_press[1])
    else:
        key_to_press = client_socket.recv(64).decode()