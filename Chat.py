import socket
import sys
import re
import threading

#class of users
class users:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

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
    #conditions
    #valid IP
    #valid Port
    c.connect((ip_destination, port_destination))#connect to client

    #add array to list
    usersList.append(users(ip_destination, port_destination))

def list(self):
    return

def terminate(connection_id):
    return

def send(connection_id, message):
    return

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
    message = ''

    #loops till user exits
    while(UserChoice != "exit"):

        #gets input
        UserChoice = input("Select from the options above: ")
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
            case ["send", connection_id, message]:
                send(connection_id, message)
            case ["exit"]:
                exit(0)
            case _:
                print("Invalid input. Type 'help' to see options\n")

#main
if __name__ == "__main__":
    #number of CL args
    n = len(sys.argv)

    #client SOCK_STREAM for TCP connection
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #server SOCK_STREAM for TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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