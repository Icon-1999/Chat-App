import socket
import os

def help():
    print("1. help\n" + 
          "2. myip\n" + 
          "3. myport\n" + 
          "4. connect <destination> <port no>\n" + 
          "5. list\n" +
          "6. terminate <connection id.>\n" +
          "7. send <connection id.> <message>\n"
          "8. exit\n")
    
def myip():
    import socket
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    ## printing the ip_address
    print(f"IP Address: {ip_address}")

def myport():
    stuff

def connect(destination, port):
    stuff

def list():
    stuff

def terminate(connection_id):
    stuff

def send(connection_id, message):
    stuff

def exit():
    stuff
    
    
def UI():
    help()
    UserChoice = input("\n")
    while(UserChoice != "exit"):
        match UserChoice:
            case "help":
                help()
            case "myip":
                myip()
            case "myport":
                myport()
            case "connect":
                connect(destination, port)
            case "list":
                list()
            case "terminate":
                terminate(connection_id)
            case "send":
                send(connection_id, message)
            case "exit":
                exit()
            case _:
                print("invalid input please choose from the choices above\n")
                help()
        
        help()
        UserChoice = input("\n")

UI()
