import socket
import time
import platform  # Zum Abrufen des PC-Namens

def get_pc_name():
    """Gibt den Namen des PCs zurück."""
    return platform.node()  # Holt den Hostnamen des PCs

def connect_to_server(server_ip):
    """Sendet die IP-Adresse, den PC-Namen und den Programmstatus an den Server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 12345))

    # Holen des PC-Namens und Setzen des Status (Programm läuft im Hintergrund)
    client_ip = socket.gethostbyname(socket.gethostname())
    pc_name = get_pc_name()
    program_status = "Active"  # Das Programm läuft, wenn dieses Skript ausgeführt wird

    # Sende die relevanten Daten an den Server
    client_socket.send(f"{client_ip},{pc_name},{program_status}".encode())

    while True:
        time.sleep(10)  # Sende alle 10 Sekunden eine Statusmeldung
        client_socket.send(f"{client_ip},{pc_name},{program_status}".encode())

# Ersetze dies mit der IP des Haupt-PCs
server_ip = "192.168.2.193"  # Haupt-PC IP-Adresse
connect_to_server(server_ip)
