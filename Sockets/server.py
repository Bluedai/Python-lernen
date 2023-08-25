import socket

def main():
    # Einstellungen für die Verbindung
    host = 'localhost'  # Ändern Sie dies auf Ihre IP-Adresse, wenn Sie das erste Programm auf einem anderen Computer ausführen
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)

        print("Warte auf Verbindung...")
        connection, address = server_socket.accept()
        print(f"Verbunden mit {address}")

        try:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                key_pressed = data.decode()
                print(f"Empfangene Taste: {key_pressed}")

                # Hier könnten Sie die empfangenen Daten verarbeiten, falls gewünscht

                # Beispiel: Daten zurück an den Client senden (Programm 1)
                connection.sendall(f"Verarbeitete Daten: {key_pressed}".encode())

        except KeyboardInterrupt:
            print("\nVerbindung wurde getrennt.")
        finally:
            connection.close()

if __name__ == "__main__":
    main()
