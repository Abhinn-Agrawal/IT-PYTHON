#Remote Code Execution
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #by default tcp protocol 
                # IP ADDRESS^       PROTOCOL^
#target ip address
target_ip = "10.1.0.234"
target_port = 9999
final_target = (target_ip, target_port)
msg = input("Please enter your message:")
#since python3 is supporting minimum encoding
new_msg = msg.encode('ascii')
#finally let's send data
s.sendto(new_msg,final_target)
