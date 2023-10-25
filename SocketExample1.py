import socket
import ipaddress
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM for TCP connection

print(s)

server = 'google.com' #can be IP address**
port = 80

server_ip = socket.gethostbyname(server) #gets IP from host name

while True:
    try:
        a = ipaddress.ip_address(server_ip)
        break
    except ValueError:
        continue

if re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', server_ip):
    ipaddress.ip_address(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"#possibly message?

s.connect(("google.com", port))#connect to client?
s.send(request.encode())#encode when send and receive
result = s.recv(4096)

print(result)

#buffering
while (len(result) > 0):
    print(result)
    result = s.recv(4096)