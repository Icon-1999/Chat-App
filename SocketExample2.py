import socket
import sys

# get the hostname
hostname = socket.gethostname()
# get the IP address
my_ip_address = socket.gethostbyname(hostname)

print('localhost')

HOST = my_ip_address #any working ip
PORT = 4445
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
	
print('Socket bind complete')

s.listen(10)

conn, addr = s.accept()

print('Connected with ' + addr[0] + ':' + str(addr[1]))

# receive message string from
# server, at a time 1024 B
msg = s.recv(1024)
  
# repeat as long as message
# string are not empty
while msg:
    print('Received:' + msg.decode())
    msg = s.recv(1024)
 
# disconnect the client
s.close()