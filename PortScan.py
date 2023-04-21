import socket

testSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

potential_Host = str(input("Would you like to enter and ip address(1) or use localhost(2)? "))
port_num = input("Enter the maximum port number and we'll scan from 0: ")
#port_Range(range(port_num))

if potential_Host == "1":
    custom_Address = input("Custom Address: ")
if potential_Host == "2":
    custom_Address = "127.0.0.1"


for x in range(0, int(port_num) + 1):
    check_Socket = testSocket.connect_ex((custom_Address, x))
    if check_Socket == 0:
        print("Port", x, "is open.")
    else:
        print("Port", x, "is closed.")

#localHost = (custom_Address, range(port_num))
#scanResult = testSocket.connect_ex(localHost)

#print(scanResult)