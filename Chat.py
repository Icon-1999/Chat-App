import socket
import sys
import os


n = len(sys.argv)

if (n != 2):
    print("Invalid amount of arguments\n" + "try 'python Chat.py <port no>'\n")
    exit(0)

port = int(sys.argv[1])

def help():
    print("\n")
    print("1. help\n"
          "2. myip\n"
          "3. myport\n"
          "4. connect <destination> <port no>\n"
          "5. list\n"
          "6. terminate <connection id.>\n"
          "7. send <connection id.> <message>\n"
          "8. exit\n")
    
def myip():
    # get the hostname
    hostname = socket.gethostname()
    # get the IP address
    ip_address = socket.gethostbyname(hostname)
    # print ip_address
    print(f"your IP Address is: {ip_address}")

def myport():
    print(f"Your port number is: {port}")

def connect(destination, port):
    stuff

def list():
    stuff

def terminate(connection_id):
    stuff

def send(connection_id, message):
    stuff
    
    
def UI():
    help()
    UserChoice = ''

    while(UserChoice != "exit"):

        UserChoice = input("Select from the options above: ")

        match UserChoice:
            case "help":
                help()
            case "myip":
                myip()
                help()
            case "myport":
                myport()
                help()
            case "connect":
                connect(destination, port)
                help()
            case "list":
                list()
                help()
            case "terminate":
                terminate(connection_id)
                help()
            case "send":
                send(connection_id, message)
                help()
            case "exit":
                exit(0)
            case _:
                print("invalid input please choose from the choices above\n")
                help()

def Main():
    if((port <= 0) or (port >= 5000)):
        print("Invalid input\n" + "Port number must be between 1 and 4999")
        return
    else:
        UI()

Main()
