import json
import socket

#target_host = "www.google.com"
target_host = "127.0.0.1"
target_port = 9998

# Create a socket object
# Learning note: AF_INET indicates use of standard IPv4 or hostname, SOCK_STREAM indicates TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host,target_port))

# Send some data
#client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.send(b"Kapow!")


# Receive some data
response = client.recv(4096)

print(response.decode())
client.close