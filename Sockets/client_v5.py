import socket
# import random
import time
import threading
import json

# Konfiguration
server_ip = '85.214.122.18'
server_ip = '192.168.178.20'
server_port = 12345

# globale Variablen initialisieren
pingzeit = ''
latenz = ''

def receive_result(client_socket):
    while True:
        try:
            result_data = client_socket.recv(1024)
            if not result_data:
                break
            result = json.loads(result_data.decode())
            process_data(client_socket, result)
        except socket.timeout:
            print("Timeout: receive_result")
            break
        except Exception as e:
            print(f"Fehler beim Empfangen von Daten vom Server: {e}")
            break
    print("receive_result Thread beendet")


# Empfangene Daten vom Server verarbeiten
def process_data(client_socket, received_data):
    if received_data["tag"] == "pong":
        global latenz
        # latenz = round((time.time() - pingzeit) * 1000,2)
        latenz = (time.time() - pingzeit) * 1000
        print(f"Latenz: {latenz:.2f} ms" )
    else:
        print(f"Unbekannte Daten vom Server: {received_data}")


# JSON Daten erstellen
def create_json_data(tag, message):
    json_str = { "tag": tag, "message": message }
    json_data = json.dumps(json_str)
    return json_data

# Daten an Server senden
def send2server(client_socket, tag, message):
    json_data = create_json_data(tag, message)
    try:
        client_socket.send(json_data.encode())
    except socket.timeout:
        print("Timout: send tag: ", tag, " message: ", message)
    except Exception as e:
        print(f"Fehler beim Senden von Daten an den Server: {e}")

# Ping an Server senden
def server_ping(client_socket):
    global pingzeit
    while True:
        time.sleep(5)
        if client_socket.fileno() == -1:
            print("Verbindung zum Server verloren. Ping Thread wird beendet")
            break
        pingzeit = time.time()
        send2server(client_socket, "ping", "ping")

# Hauptprogramm
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    client.settimeout(20)  # Timeout von 20 Sekunden
    threads = []

    # Daten Vom Server Thread starten
    result_thread = threading.Thread(target=receive_result, args=(client,))
    threads.append(result_thread)
    result_thread.start()

    # Ping Thread starten
    ping_thread = threading.Thread(target=server_ping, args=(client,))
    threads.append(ping_thread)
    ping_thread.start()

    # Warten solange noch Threads aktiv sind
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
