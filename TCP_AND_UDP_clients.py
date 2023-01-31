
from http import client
import socket

target="www.google.com"
port=8080
target1="127.0.0.1"


#TCP
try:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((target,port))
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    print(client.recv(4096))
except:
    print("Conn refused")





#UDP
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.connect((target1,port))
client.sendto(b"AAABBBCCC",(target1,port))
data,addr = client.recvfrom(4096)
print(data)
