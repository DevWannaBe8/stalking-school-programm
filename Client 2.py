import socket
import platform
import os

class Client:
    def __init__(self, server_ip='YOUR IP !!!!!!!!', server_port=65432):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket.connect((self.server_ip, self.server_port))

    def send_message(self, message):
        """Sendet eine Nachricht an den Server"""
        self.client_socket.send(message.encode('utf-8'))

    def listen_for_commands(self):
        """Hört auf Befehle vom Server und führt diese aus"""
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message == "systeminfo":
                    info = f"OS: {platform.system()} {platform.release()}, IP: {self.get_ip()}"
                    self.client_socket.send(info.encode('utf-8'))
                elif message == "standby":
                    os.system("shutdown -h now")  # Standby-Befehl
                elif message == "restart":
                    os.system("shutdown /r /f /t 0")  # Neustart-Befehl
                elif message == "disconnect":
                    break
                elif message == "uninstall":
                    self.client_socket.send("Deinstalliere Programm...".encode('utf-8'))
                    break
            except Exception as e:
                print(f"Fehler: {e}")
                break
        self.client_socket.close()

    def get_ip(self):
        """Holt die IP des Clients"""
        return os.popen('ipconfig getifaddr en0').read().strip()

if __name__ == "__main__":
    client = Client()
    client.listen_for_commands()
