#!/usr/bin/env python3
from tkinter import *
import tkinter.messagebox as mbox
import socket
import pickle

"""
@note This script uses tkinter to create a GUI for a client user. It's buttons will be connected with command towards 
the functions within the script.
add_stockitem takes the input given and pickles it before sending to the server
close_program will shut down the client script
message_box will display a popup when the pickled data is sent
The script also uses socket module to be able to connect to a listening side
"""


def add_stockitem():  # Here the input made from the client will be pickled and sent to the server
    transfer_data = list()
    transfer_data.append(ent_code.get() + ent_description.get() + ent_amount.get())
    print(transfer_data)  # list have been created and showed
    pickled = pickle.dumps(transfer_data)  # list => bytes
    print(pickled)
    client.send(pickled)  # bytes are sent.
    message_box()


def message_box():
    mbox.showinfo("Success", "Stock item has been sent to server")


def close_program():
    mbox.showinfo("Closing", "Have a nice day")
    exit()


# Towards what server location it is searching for to create an establishment
HOST = "127.0.0.1"
PORT = 33445
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    print("Connecting...")
    client.connect((HOST, PORT))
    data = client.recv(1024)
    print("Received: ", data)
    client.sendall(b"Client have successfully connected to server")


# This section is defining the window, button an input location for the GUI
window = Tk()
window.title("Add the stock item to the server")
window.geometry("400x200")
window.configure(bg="lightblue")

# lbl = label, ent = input
lbl_code = Label(window, text="Code:")
lbl_code.place(x=5, y=10)
ent_code = Entry(window)
ent_code.place(x=150, y=5)

lbl_description = Label(window, text="Description:")
lbl_description.place(x=5, y=40)
ent_description = Entry(window)
ent_description.place(x=150, y=35)

lbl_amount = Label(window, text="Amount:")
lbl_amount.place(x=5, y=70)
ent_amount = Entry(window)
ent_amount.place(x=150, y=65)

# btn = button
btn_submit = Button(window, text="Submit", command=add_stockitem)
btn_submit.place(x=300, y=65)

btn_close = Button(window, text="Close", command=close_program)
btn_close.place(x=300, y=95)

window.mainloop()

