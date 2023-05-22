import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto('Hello'.encode('utf-8'), ('192.168.0.10', 123))
data, address = s.recvfrom(4096)
print("UTC: ", data.decode('utf-8'), "\n\n")
s.close()
