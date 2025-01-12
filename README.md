# stalking-school-programm
# Client-Server Management Tool

This is an example of a **Client-Server Management Tool**, which allows you to remotely manage clients and execute various commands. The tool consists of a server and a client script that enable the following actions:

- **Retrieve System Information**
- **Put PC in Standby**
- **Restart PC**
- **Send Messages to Clients**
- **Start Remote Desktop**
- **Disconnect and Reconnect Clients**
- **Uninstall the Program**

**Important Notice:** This tool must only be used in a legally compliant environment and with the explicit consent of the owner of the respective computer. Misuse of this tool may result in legal consequences.

## Prerequisites

- **Python 3.x** must be installed on the system.
- **tkinter** and **socket** (usually pre-installed with Python).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/Client-Server-Management-Tool.git

    Install dependencies (usually pre-installed):

    pip install -r requirements.txt

Usage
Starting the Server

    To start the server, run the following command:

    python server.py

    The server will open a graphical user interface (GUI) with a table displaying all connected clients. You can right-click on a client to perform actions like "Show System Info", "Restart PC", "Start Remote Desktop", and more.

Starting the Client

    To start the client, run the following command:

    python client.py

    The client will connect to the server and wait for commands. After the connection, it will execute commands from the server, such as retrieving system information or restarting the PC.

Features
Server:

    Show System Information: Displays system information of the client.
    Put PC in Standby: Puts the client PC in standby mode.
    Restart PC: Restarts the client PC.
    Send Message: Sends a message to the client.
    Start Remote Desktop: Starts a remote desktop session with the client.
    Disconnect Client: Disconnects a client.
    Reconnect Client: Reconnects a client.
    Uninstall: Uninstalls the program from the client.

Client:

    Command Execution: The client listens for commands from the server and executes them:
        Retrieve System Info.
        Put PC in Standby.
        Restart PC.
        Disconnect or Uninstall.

Disclaimer

WARNING: The developer of this tool assumes no responsibility for misuse, unauthorized access, or other illegal activities resulting from the use of this tool. This tool may only be used in a controlled and legally secure environment. Any misuse or use of this tool without the consent of the system owner is illegal and may be subject to legal action.

Use at your own risk. The developer is not liable for any damages, data loss, or other negative consequences resulting from the use of this program.
License

This project is licensed under the MIT License. For more information about licensing, please refer to the LICENSE file in the repository.
Issues and Support

If you encounter issues or need support, please open an Issue on GitHub.
Contributors

    [WannaBe] - Main Developer


### Explanation:

1. **Liability Disclaimer:** It's clearly stated that the user uses this tool at their own risk and that it should only be used with the explicit consent of the system owner.
2. **License:** The project is licensed under the **MIT License**, meaning it can be used and modified freely but with no liability.
3. **Warning:** It explicitly mentions that misuse of the tool is illegal and may result in legal consequences.
   
### Notes:
- **Repository URL:** Make sure to update the repository URL in the "Installation" section to your actual GitHub repository URL.
- **Dependencies:** If you have additional libraries or requirements, you can list them in a `requirements.txt` file and specify them here.

This README file provides all the necessary information while also protecting you legally.

