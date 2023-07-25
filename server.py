import threading
import socket
import tkinter as tk
from tkinter import messagebox

host = '192.168.4.2'
port = 55555

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server.bind((host, port))

# Listen for incoming connections
server.listen()

# Lists to keep track of connected clients and their nicknames
clients = []
nicknames = []

# Variable booleana para controlar el estado del servidor
server_running = True

def broadcast(message):
    # Send a message to all connected clients
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            # Receive a message from the client
            message = client.recv(1024)
            
            # Broadcast the message to all clients
            broadcast(message)
        except:
            # If there's an error receiving the message, handle client disconnection
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'1 person left the chat'.encode('utf-8'))
            break

def receive():
    while server_running:
        try:
            # Accept a new client connection
            client, address = server.accept()
            print(f'Connected with {str(address)}')

            # Request the client to provide a nickname
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            
            # Add the client and their nickname to the lists
            nicknames.append(nickname)
            clients.append(client)

            print(f'Nickname of the client is {nickname}')
            
            # Broadcast a message to all clients that a new client has joined
            broadcast('1 person joined the chat'.encode('utf-8'))
            
            # Send a welcome message to the connected client
            client.send('Connected to the server!'.encode('utf-8'))

            # Create a new thread to handle the client
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except OSError:
            # Si el socket se ha cerrado, salir del bucle
            break

# Función para detener el servidor
def stop_server():
    global server_running
    result = messagebox.askquestion("Confirmar", "¿Estás seguro que deseas detener el servidor, eso detiene la comunicación?")
    if result == "yes":
        server_running = False
        server.close()
        root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Servidor-LaDyR-2023")

# Agregar un Label para mostrar el texto "SERVIDOR EJECUTÁNDOSE..."
label = tk.Label(root, text="SERVIDOR EJECUTÁNDOSE...", font=("Arial", 20))
label.pack(pady=20)

# Agregar un botón para detener el servidor
stop_button = tk.Button(root, text="Detener Servidor", command=stop_server)
stop_button.pack(pady=20)

# Iniciar el hilo del servidor
server_thread = threading.Thread(target=receive)
server_thread.start()

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
