#!/usr/bin/env python3
from Course_Project import StockClass
from datetime import date
import socket
import threading
import pickle

secret = 'Administrator'  # Password  authentication section. PS. bad location practise IRL, and not mentioned in report

tc = StockClass.StockTracker()  # Shorting the path pointer towards StockTracker class

time = date.today()  # taking use of today's date from computer and gives it a output structure
log = time.strftime("%d/%m/%Y")

# The menu panel is added to a txt file, to minimize amount of text in script
print("\nWelcome. Choose what you want to do", "\n-------------------------------------")
read_main_panel = open("main_panel.txt", "r")
main_panel = read_main_panel.read()

"""
@note This class represents the server itself, holding a constructor which creates 2 separate threads for multi 
process purpose.
The server_thread will manage the input choices made from the user.
The client_thread will use a socket and listen for a client connection attempt
"""


# A class for the server is created, this to manage a threading so that both server and client wont collide
class Server:

    def __init__(self):  # making a constructor for the threading
        self.client_thread = threading.Thread(target=self.listening)
        self.server_thread = threading.Thread(target=self.server_work)
        self.server_thread.start()
        self.client_thread.start()

    def server_work(self):  # A while loop is created, as long as choice is not 6, the loop will continue
        destination = True
        while destination:
            print("log =", log)
            print(main_panel)
            choice = input(":")
            if choice == "6":
                tc.save_list()
                print("StockItem list has been saved to the csv file\b, Have a nice day")
                destination = False
            else:
                if choice == "1":  # takes the inputs and connecting them to values that's sent to StockTracker class
                    print("#1 Add a stock item", "\n---------------------")
                    print("Add code:")
                    code = input("")
                    print("Add description:")
                    description = input("")
                    print("Add amount:")
                    amount = input("")
                    tc.add_stock(code, description, amount)

                if choice == "2":
                    print("#2 Update a stock item", "\n---------------------")
                    print("What stock to update?:")
                    tc.update_stock()

                if choice == "3":
                    print("#3 Display detail of a stock", "\n---------------------")
                    print("What stock to display?: ")
                    tc.search_index()

                if choice == "4":
                    print("#4 Display the stock list", "\n---------------------")
                    tc.show_list()

                if choice == "5":  # this option is not within the report, as it is outside the scope and incomplete
                    print("#5 Delete a stock item", "\n---------------------")
                    pw = ''  # From here the script will start the password requesting before proceeding
                    count = 0
                    max_attempt = 3
                    while pw != secret:
                        count += 1
                        if count > max_attempt:
                            print("access denied!!")
                            break
                        pw = input("Access authentication required. Insert password! :")
                    else:
                        print("What stock to delete?:")
                        tc.delete_stock()

                if choice == "6":
                    print("#6 Exit the program", "\n---------------------")
                    tc.save_list()
                    print("StockItem list has been saved to the csv file\b, Have a nice day")
                    destination = False

    def listening(self):  # This section is the listening function for the server, where it waits for a client connect
        print("\n Listening....\n")
        host = "127.0.0.1"
        port = 33445
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((host, port))
            server.listen()
            conn, addr = server.accept()
            conn.sendall(b"You've successfully connected to the StockAll server")
            data = conn.recv(1024)
            print("Received: ", data)
            while True:
                data = conn.recv(1024)  # Bytes
                if not data:
                    break
                # The input from the client will here be un-pickled and then processed just as in choice 1
                pickle_data = pickle.loads(data)  # list is unpacked
                code, description, amount = pickle_data  # the list is split
                tc.add_stock(code, description, amount)  # Sending each variable as own input


if __name__ == "__main__":  # The main is defined as the Server class
    Server()
