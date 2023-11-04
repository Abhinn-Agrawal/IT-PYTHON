import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
my_ip = "10.1.0.167"
my_port = 9999
my_address = (my_ip, my_port)
s.bind(my_address)
while 3>2:
    data = s.recvfrom(100)
    print(data)
    time.sleep(2)
