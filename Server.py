import socket
from pynput import keyboard

while True:
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.bind(('localhost', 8089))

        server_socket.listen(5) # become a server socket, maximum 5 connections

        connection, address = server_socket.accept()
        print(f"Got a connection from {address}")

        # Dictionary to track which keys are currently pressed
        pressed_keys = {}

        def on_press(key):
            try:
                key_str = str(key)  # Convert key to string representation
                if key != keyboard.Key.esc:
                    if key_str not in pressed_keys:
                        pressed_keys[key_str] = True
                        connection.send(check_special(key).encode())  # Send special key status
                        connection.send(key_str.encode())  # Send the key to the client
                else:
                    listener.stop()
            except Exception as e:
                print(f"Error in on_press: {e}")

        def on_release(key):
            try:
                key_str = str(key)
                if key_str in pressed_keys:
                    pressed_keys.pop(key_str)  # Remove the key from the pressed_keys dict
            except Exception as e:
                print(f"Error in on_release: {e}")

        def check_special(key):
            print((str(key)))
            if len(str(key)) == 3:  # If the key is a regular character (non-special)
                return 'y'  # 'y' for regular key
            print(len(str(key)))
            return 'n'  # 'n' for special key (like shift, enter, etc.)

        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.run()

        if(not listener.is_alive()):
            connection.close()

    except Exception as e:        
        print(f"Error: {e}")