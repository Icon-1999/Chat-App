import socket
import sys
import re
import threading
import shlex

class Server_Side(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((myip(), myport()))
        self.s.listen(5)
        self.connections = []
        
    # receiving incoming connection
    def receive(self, client, address):
        while True:
            try:
                data = client.recv(1024).decode()
                if data:
                    print(f"Received message from {str(address)}: {data}")
                    print(f"Sender's Port: {address[1]}")
                    print(f"Message: \"{data}\"")
                else:
                    print(f"Closed connection from {str(address)}")
                    self.connections.remove(client)
                    break
            except:
                print(f"Error receiving message from {str(address)}")
                self.connections.remove(client)
                break

    # runs thread and call receive
    def run(self):
        while True:
            client, address = self.s.accept()
            self.connections.append(client)
            print(f"Connected with {str(address)}")
            threading.Thread(target=self.receive, args=(client, address)).start()

#class of users
class users:
    def __init__(self, ip_address, port, connection):
        self.ip_address = ip_address
        self.port = port
        self.connection = connection

#list of users
usersList = []

def options():
    print("1. help\n"
          "2. myip\n"
          "3. myport\n"
          "4. connect <destination> <port no>\n"
          "5. list\n"
          "6. terminate <connection id.>\n"
          "7. send <connection id.> <message>\n"
          "8. exit\n")
    
def help():
    print("1. 'help' - Displays information about the available user interface options or command manual.\n\n"
          
          "2. 'myip'- Displays your IP address of this process.\n\n"

          "3. 'myport' - Displays your port on which this process is listening for incoming connections.\n\n"

          "4. 'connect <destination> <port no>' - This command establishes a new TCP connection to the specified\n"
            "<destination> at the specified <port no>. The <destination> is the IP address of the receiver's computer.\n"
            "The <port no> is the receiver's port number that is waiting for incoming TCP connection\n\n"

          "5. 'list' - Displays a numbered list of all the connections this process is part of. This numbered list will\n"
            "include connections initiated by this process and connections initiated by other processes.\n\n"

          "6. 'terminate <connection id.>' - This command will terminate the connection listed under the specified\n"
            "<connection id.> when LIST is used to display all connections. E.g., terminate 2. In this example, the\n"
            "connection with 192.168.21.21 should end.\n\n"

          "7. 'send <connection id.> <message>'- This will send the message to the host on the connection that is\n"
            "designated by the number <connection id.> when command “list” is used. The message to be sent can be up-to\n"
            "100 characters long, including blank spaces.\n\n"

          "8. 'exit' - Close all connections and terminate this process.\n\n")
    
def myip():
    # get the hostname
    hostname = socket.gethostname()
    # get the IP address
    my_ip_address = socket.gethostbyname(hostname)
    return my_ip_address

def myport():
    return my_port

def connect(ip_destination, port_destination):
    try:
        c.connect((ip_destination, port_destination))  # connect to client
        usersList.append(users(ip_destination, port_destination, c))
    except Exception as e:
        print(f"Error connecting to {ip_destination}:{port_destination}: {e}")

def list():
    print("List of all connections:")
    for i, user in enumerate(usersList, 1):
        print(f"{i}. {user.ip_address}:{user.port}")

def terminate(connection_id):
    if not connection_id.isdigit():
        print("Invalid connection ID. Please enter a valid number.")
        return

    index = int(connection_id) - 1

    if index < 0 or index >= len(usersList):
        print("Invalid connection ID. Please use 'list' to see available connections.")
        return

    try:
        user = usersList[index]
        user.connection.close()
        del usersList[index]
        print(f"Connection {connection_id} terminated.")
    except Exception as e:
        print(f"Error terminating connection: {e}")

def send(connection_id, message):
    if int(connection_id) > len(usersList) or int(connection_id) < 1:
        print("Invalid connection ID. Please use 'list' to see available connections.")
        return

    try:
        index = int(connection_id) - 1
        user = usersList[index]
        c.sendall(message.encode())
        print(f"Message sent to Connection ID: {connection_id}")
    except:
        print("Error sending message.")
    

def validIP(ip):
    while True:
        #if valid ip the return ip
        if re.match(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$', ip): #regex to check valid ip
            print("valid IP address")
            return ip
        else:
            #if not then prompt error and retry
            print("Invalid IP address format\n" + "Should look like: 192.0.1.1\n")
            ip = input('Re-enter IP address: ')

def validPort(port):
    while True:
        #if valid port the return port
        if((port > 0) and (port < 5000)):
            print("\nvalid port number\n")
            return port
        else:
            #if not then prompt error and retry
            print("Invalid port number\n" + "Port number must be between 1 and 4999\n")
            port = int(input('Re-enter port number: '))

def UI():
    options()
    #variables for functions
    UserChoice = ''
    connection_id = ''
    destination_ip = ''
    destination_port = ''
    #message = ''

    try:
        t = Server_Side()
        t.daemon = True
        t.start()
        #loops till user exits
        while 1:

            #gets input
            UserChoice = input("")
            #splits input into array of strings so code can check for multiple args
            input_choice = UserChoice.split()

            #case for input_choice array
            match input_choice:
                case ["help"]:
                    help()
                case ["myip"]:
                    # print ip_address
                    print(f"your IP Address is: {myip()}")
                case ["myport"]:
                    print(f"Your port number is: {myport()}")
                case["connect", destination_ip, destination_port]:
                    #changes destination port from str to int
                    destination_port = int(destination_port)
                    #gets/checks valid destination IP from user
                    destination_ip = validIP(destination_ip)
                    #gets/checks valid destination port from user
                    destination_port = validPort(destination_port)
                    #calls connect
                    connect(destination_ip, destination_port)
                case ["list"]:
                    list()
                case ["terminate", connection_id]:
                    terminate(connection_id)
                case ["send", connection_id]:
                    message = input("Enter your message: ")
                    send(connection_id, message)
                case ["exit"]:
                    exit(0)
                case _:
                    print("Invalid input. Type 'help' to see options\n")
    except KeyboardInterrupt:
        print("Done!")

#main
if __name__ == "__main__":
    #number of CL args
    n = len(sys.argv)

    #client SOCK_STREAM for TCP connection
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    #checks valid number of CL args
    if (n != 2):
        print("Invalid amount of arguments\n" + "try 'python Chat.py <port no>'\n")
        exit(0)

    #gets port number from CL arg
    my_port = int(sys.argv[1])

    #gets/checks valid port from user
    my_port = validPort(my_port)

    
    #calls UI
    UI()

    exit(0)