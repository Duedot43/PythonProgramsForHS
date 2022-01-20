# Import socket module
import socket			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 25565			

# connect to the server on local computer
s.connect(('127.0.0.1', port))
#s.send("1")
# receive data from the server and decoding to get the string.
wait =  (s.recv())
game = 1
while game == 1:
    if wait == 1:
        print("Waiting...")
    else:
        #Start the game
        print(".")
# close the connection
s.close()