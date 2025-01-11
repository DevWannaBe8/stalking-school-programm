import tkinter as tk
from tkinter import ttk
import socket
import threading
from tkinter import messagebox

class ClientManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Manager")

        # Treeview to show clients and additional information
        self.tree = ttk.Treeview(root, columns=("IP", "Country", "User Status", "Connection Status", "User@PC"), show="headings")
        
        # Define the column headings
        self.tree.heading("IP", text="IP Adresse")
        self.tree.heading("Country", text="Land")
        self.tree.heading("User Status", text="Benutzerstatus")
        self.tree.heading("Connection Status", text="Verbindungsstatus")
        self.tree.heading("User@PC", text="User@PC")
        
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Dictionary to store client data with IP as key
        self.client_data = {}

    def add_client(self, client_ip, country, user_status, connection_status, user_pc):
        """Add new client details to the treeview."""
        self.tree.insert("", "end", values=(client_ip, country, user_status, connection_status, user_pc))

    def update_client_status(self, client_ip, country, user_status, connection_status, user_pc):
        """Update an existing client's details in the treeview."""
        for item in self.tree.get_children():
            if self.tree.item(item, "values")[0] == client_ip:
                self.tree.item(item, values=(client_ip, country, user_status, connection_status, user_pc))

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 12345))  # Bind to all available IPs
        server_socket.listen(5)
        print("Server läuft und wartet auf Verbindungen...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Verbindung von {client_address}")
            client_ip = client_address[0]
            
            # Empfange die Client-Daten (IP, PC-Name, Programmstatus)
            data = client_socket.recv(1024).decode()
            client_ip, pc_name, program_status = data.split(',')

            # Simuliere Land (dies könnte durch GeoIP ermittelt werden)
            country = "Germany"  # Platzhalter für Land
            user_status = "Active" if program_status == "Active" else "Inactive"
            connection_status = "Connected" if program_status == "Active" else "Disconnected"
            user_pc = f"{pc_name}@{client_ip}"

            # Aktualisiere oder füge den Client in die Tabelle ein
            if client_ip not in self.client_data:
                self.add_client(client_ip, country, user_status, connection_status, user_pc)
            else:
                self.update_client_status(client_ip, country, user_status, connection_status, user_pc)

            threading.Thread(target=self.handle_client, args=(client_socket, client_address, client_ip)).start()

    def handle_client(self, client_socket, client_address, client_ip):
        """Handle communication with the connected client."""
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"Nachricht von {client_address}: {message}")
            except:
                break

        # Wenn der Client die Verbindung trennt, aktualisiere den Status
        print(f"Client {client_ip} disconnected.")
        self.update_client_status(client_ip, "Germany", "Inactive", "Disconnected", f"User@{client_ip}")
        client_socket.close()

# Setup the main window
root = tk.Tk()
app = ClientManagerApp(root)

# Start server in a separate thread
server_thread = threading.Thread(target=app.start_server)
server_thread.daemon = True
server_thread.start()

root.mainloop()
