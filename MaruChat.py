import socket
import threading
import tkinter as tk
from PIL import Image, ImageTk
from time import sleep

host = '127.0.0.1'
port = 55555
nickname = "Guest" # Default nickname

def client_req(host, port, nickname):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    def receive():
        while True:
            try:
                message = client.recv(1024).decode('ascii')
                if message == 'NICK':
                    client.send(nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print('An error occurred')
                client.close()
                break

    def write():
        while True:
            message = f'{nickname}: {input("")}'
            client.send(message.encode('ascii'))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

def black_button_click():
    label.config(text="Joined room!")
    black_button.destroy()
    button.destroy()
    entry.destroy()
    client_req(host, port, nickname)

def change_nickname():
    new_nickname = entry.get()  # Get the new nickname from the entry widget
    global nickname
    nickname = new_nickname  # Update the global nickname variable
    label.config(text="Nickname: " + nickname)  # Update the label text


# Create the main window
window = tk.Tk()
window.title("MaruChat")  # Set the window title

# Set the window background color
window.configure(bg="white")

# Load and resize the logo image
logo_image = Image.open("logo.png")  # Replace "logo.png" with your image file
logo_image = logo_image.resize((200, 200))  # Adjust the size as per your image requirements

# Create an ImageTk object for the logo image
logo_image_tk = ImageTk.PhotoImage(logo_image)

# Create a label widget for the logo image
logo_image_label = tk.Label(window, image=logo_image_tk, bg="white")
logo_image_label.pack()

# Load and resize the type GIF
type_gif = Image.open("type.gif")  # Replace "type.gif" with your GIF file
type_gif = type_gif.resize((100, 100))  # Adjust the size as per your GIF requirements

# Create an ImageTk object for the type GIF
type_gif_tk = ImageTk.PhotoImage(type_gif)

# Create a label widget for the type GIF
type_gif_label = tk.Label(window, image=type_gif_tk, bg="white")
type_gif_label.place(x=window.winfo_screenwidth() - 100, y=window.winfo_screenheight() - 100, anchor="se")

# Keep a reference to the GIF image
type_gif_label.image = type_gif_tk

# Create a label widget
label = tk.Label(window, text="Welcome! "+nickname, bg="white", fg="black")
label.pack()

# Create a red button widget
#red_button = tk.Button(window, text="Host as server", command=red_button_click, bg="red", fg="white")
#red_button.pack()

# Create an entry widget for entering the new nickname
entry = tk.Entry(window)
entry.pack()

# Create a button to change the nickname
button = tk.Button(window, text="Change Nickname", command=change_nickname, bg="red", fg="white")
button.pack()

# Create a black button widget
black_button = tk.Button(window, text="Join room!", command=black_button_click, bg="black", fg="white")
black_button.pack()

# Create a label widget for the copyright text
copyright_label = tk.Label(window, text="© 2023 MARUCHAT. All rights reserved.", bg="white", fg="gray") # funny haha
copyright_label.pack()

# Start the GUI event loop
window.mainloop()


