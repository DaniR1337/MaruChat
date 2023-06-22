import threading
import socket

host = '127.0.0.1'
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
    while True:
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

# Start the server and wait for connections
print('Server is running')
receive()
