import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import socket
import threading
import platform


class Server:
    def __init__(self, host='127.0.0.1', port=65432):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.clients = []  # Liste der Clients (Verbindungen)
        self.root = tk.Tk()
        self.root.title("Client Manager")
        
        self.tree = ttk.Treeview(self.root, columns=("IP", "Country", "User Status", "Connection Status", "User@PC"), show="headings")
        self.tree.heading("IP", text="IP Adresse")
        self.tree.heading("Country", text="Land")
        self.tree.heading("User Status", text="Benutzerstatus")
        self.tree.heading("Connection Status", text="Verbindungsstatus")
        self.tree.heading("User@PC", text="User@PC")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Systeminformationen", command=self.show_system_info)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="PC in Standby", command=self.pc_standby)
        self.context_menu.add_command(label="PC Neustarten", command=self.pc_restart)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Nachricht senden", command=self.show_message_box)
        self.context_menu.add_command(label="Remote Desktop starten", command=self.remote_desktop)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Trennen", command=self.disconnect_client)
        self.context_menu.add_command(label="Reconnect", command=self.reconnect_client)
        self.context_menu.add_command(label="Deinstallieren", command=self.uninstall_client)

        self.tree.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.context_menu.post(event.x_root, event.y_root)

    def show_system_info(self):
        selected_item = self.tree.selection()
        client_ip = self.tree.item(selected_item, "values")[0]
        for client_socket, client_address in self.clients:
            if client_address[0] == client_ip:
                client_socket.send("systeminfo".encode('utf-8'))
                response = client_socket.recv(1024).decode('utf-8')
                messagebox.showinfo("Systeminformationen", response)
                break

    def pc_standby(self):
        selected_item = self.tree.selection()
        client_ip = self.tree.item(selected_item, "values")[0]
        for client_socket, client_address in self.clients:
            if client_address[0] == client_ip:
                client_socket.send("standby".encode('utf-8'))
                messagebox.showinfo("Aktion", f"PC {client_ip} in Standby versetzen...")
                break

    def pc_restart(self):
        selected_item = self.tree.selection()
        client_ip = self.tree.item(selected_item, "values")[0]
        for client_socket, client_address in self.clients:
            if client_address[0] == client_ip:
                client_socket.send("restart".encode('utf-8'))
                messagebox.showinfo("Aktion", f"PC {client_ip} wird neu gestartet...")
                break

    def show_message_box(self):
        selected_item = self.tree.selection()
        client_ip = self.tree.item(selected_item, "values")[0]
        messagebox.showinfo("Nachricht senden", f"Nachricht an {client_ip} senden...")

    def remote_desktop(self):
        selected_item = self.tree.selection()
        client_ip = self.tree.item(selected_item, "values")[0]
        messagebox.showinfo("Remote Desktop", f"Starte Remote Desktop zu {client_ip}...")

    def disconnect_client(self):
        selected_item = self.tree.selection()
        client_ip = self.tree.item(selected_item, "values")[0]
        for client_socket, client_address in self.clients:
            if client_address[0] == client_ip:
                client_socket.send("disconnect".encode('utf-8'))
                messagebox.showinfo("Verbindung trennen", f"Client {client_ip} wird getrennt...")
                break

    def reconnect_client(self):
        selected_item = self.tree.selection()
        client_ip = self.tree.item(selected_item, "values")[0]
        for client_socket, client_address in self.clients:
            if client_address[0] == client_ip:
                client_socket.send("reconnect".encode('utf-8'))
                messagebox.showinfo("Verbindung wiederherstellen", f"Stelle Verbindung zu {client_ip} wieder her...")
                break

    def uninstall_client(self):
        selected_item = self.tree.selection()
        client_ip = self.tree.item(selected_item, "values")[0]
        for client_socket, client_address in self.clients:
            if client_address[0] == client_ip:
                client_socket.send("uninstall".encode('utf-8'))
                messagebox.showinfo("Deinstallation", f"Deinstalliere das Programm von {client_ip}...")
                break

    def handle_client(self, client_socket, client_address):
        self.clients.append((client_socket, client_address))
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break

                if message == "systeminfo":
                    client_socket.send(f"OS: {platform.system()} {platform.release()}".encode('utf-8'))
                elif message == "standby":
                    client_socket.send("PC in Standby...".encode('utf-8'))
                elif message == "restart":
                    client_socket.send("PC wird neu gestartet...".encode('utf-8'))
                elif message == "disconnect":
                    client_socket.send("Verbindung wird getrennt...".encode('utf-8'))
                    break
                elif message == "reconnect":
                    client_socket.send("Verbindung wird wiederhergestellt...".encode('utf-8'))
                elif message == "uninstall":
                    client_socket.send("Deinstalliere Programm...".encode('utf-8'))
            except Exception as e:
                break
        client_socket.close()

    def start_server(self):
        print("Server gestartet und wartet auf Verbindungen...")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Verbindung von {client_address} hergestellt.")
            threading.Thread(target=self.handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    server = Server()
    threading.Thread(target=server.start_server).start()
    server.root.mainloop()
