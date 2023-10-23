import socket
import sys
import os

n = len(sys.argv)

if (n != 2):
    print("Invalid amount of arguments\n" + "try 'python Chat.py <port no>'\n")
    exit(0)

my_port = int(sys.argv[1])

def options():
    print("\n")
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
    # print ip_address
    print(f"your IP Address is: {my_ip_address}")

def myport():
    print(f"Your port number is: {my_port}")

def connect(ip_destination, port_destination):
    stuff

def list():
    stuff

def terminate(connection_id):
    stuff

def send(connection_id, message):
    stuff
    

def UI():
    options()
    UserChoice = ''
    connection_id = ''
    destination_ip = ''
    destination_port = ''
    message = ''

    while(UserChoice != "exit"):

        UserChoice = input("Select from the options above: ")
        input_choice = UserChoice.split()
        print(input_choice)

        match input_choice:
            case "help":
                help()
            case "myip":
                myip()
                options()
            case "myport":
                myport()
                options()
            case["connect", destination_ip, destination_port]:
                connect(destination_ip, destination_port)
                options()
            case "list":
                list()
                options()
            case ["terminate", connection_id]:
                terminate(connection_id)
                options()
            case ["send", connection_id, message]:
                send(connection_id, message)
                options()
            case "exit":
                exit(0)
            case _:
                print("invalid input please choose from the choices above\n")
                options()

def Main():
    if((my_port <= 0) or (my_port >= 5000)):
        print("Invalid input\n" + "Port number must be between 1 and 4999")
        return
    else:
        UI()

Main()
