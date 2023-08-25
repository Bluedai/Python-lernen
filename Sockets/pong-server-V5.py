#!/usr/bin/env python3

# Imports
import socket
import threading
import time
import json

# Konfiguration
max_clients = 5
server_ip = '85.214.122.18'
server_ip = '192.168.178.20'
server_port = 12345

# dynamische Variablen und feste Vorgaben
active_clients = []                                 # Liste mit allen aktiven Clients
ac_lock = threading.Lock()                          # Lock für die Client-Verwaltung
available_ids = set(range(1, max_clients + 1))      # IDs, die noch vergeben werden können
id_lock = threading.Lock()                          # Lock für die ID-Verwaltung



# Client ID-Verwaltung
def assign_client_id():
    with id_lock:
        if available_ids:
            client_id = min(available_ids)
            available_ids.remove(client_id)
            return client_id
        return None
def release_client_id(client_id):
    with id_lock: # nicht notwendig bei einem add() auf ein set
        available_ids.add(client_id)

# Socket-Verwaltung
def add_client(client_socket):
    client_id = assign_client_id()
    if client_id is not None:
        active_clients.append((client_id, client_socket))
    else:
        print("Fehler: Keine verfügbare ID mehr!")

def remove_client(client_socket):
    for entry in active_clients:
        if entry[1] == client_socket:
            client_id = entry[0]
            active_clients.remove(entry)
            release_client_id(client_id)
            client_socket.close()
            break

# JSON Daten erstellen
def create_json_data(tag, message):
    json_str = { "tag": tag, "message": message }
    json_data = json.dumps(json_str)
    return json_data


def send2client(client_socket, tag, message):
    json_data = create_json_data(tag, message)
    try:
        client_socket.send(json_data.encode())
    except socket.timeout:
        print("Timout: send tag: ", tag, " message: ", message)

def send2all_clients(tag, message):
    # json_data = create_json_data(tag, message)
    threads = []
    for entry in active_clients:
        client_socket = entry[1]
        thread = threading.Thread(target=send2client, args=(client_socket,tag,message))
        threads.append(thread)
        thread.start()

    # auf alle Threads warten
    for thread in threads:
        thread.join()

# Empfangene Daten vom Client verarbeiten
def process_data(client_socket, received_data):
    if received_data["tag"] == "ping":
        send2client(client_socket, "pong", "pong")
    
# Verbindung zum Client
def handle_client(client_socket):
    client_socket.settimeout(20)  # Timeout von 20 Sekunden
    client_number = assign_client_id()
    if client_number is None:
        msg="Keine verfügbaren Plätze mehr! Verbindung wird geschlossen"
        send2client(client_socket, "error", msg)
        print(msg)
        client_socket.close()
        return

    active_clients.append((client_number,client_socket))
    

    # Nachricht an den Client senden, um seine Nummer mitzuteilen
    send2client(client_socket, "client_number", client_number)

    while True:
        try:
            print("Warte auf Nachricht vom Client", client_number)
            data = client_socket.recv(1024)
            
            received_data = json.loads(data.decode())
            print(f"Empfangene Daten vom Client {client_number}: {received_data} : socket: {client_socket}")
            process_data(client_socket, received_data)

        except socket.timeout:
            print(f"Timeout: Keine Nachricht vom Client {client_number} erhalten")
            break
        # alle restlichen exceptions abfangen
        except Exception as e:
            print(f"Fehler beim Empfangen von Daten vom Client {client_number}: {e}")
            break
    
    print(f"Verbindung zu Client {client_number} geschlossen:")
    remove_client(client_socket)

def display_active_connections():
    while True:
        print("Aktive Verbindungen:")
        for i, client_socket in enumerate(active_clients, 1):
            print(f"Verbindung {i}: {client_socket.getpeername()}")
        print("----------------------")
        time.sleep(10)

def main():
    # TCP server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # UDP server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    
    print("Server startet und lauscht auf Port", server_port)
    
    # display_thread = threading.Thread(target=display_active_connections)
    # display_thread.start()
    
    while True:
        client_socket, addr = server.accept()
        print("Neue Verbindung hergestellt:", addr)
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
