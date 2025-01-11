import socket
import time

def connect_to_server(server_ip):
    """Send the client's IP address to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 123456)) # Server ip u can change it to whatever you want 

    # Send the client's IP address to the server
    client_ip = socket.gethostbyname(socket.gethostname())
    client_socket.send(client_ip.encode())

    while True:
        time.sleep(10)  # Send IP address every 10 seconds (keep alive)

# Replace with the main PC's IP address
server_ip = "________________YOUR IP ADRESS______________"  # MAIN IP ADRESS YOU CAN GET IT WITH cmd command ipconfig ip4v or smt
connect_to_server(server_ip)
