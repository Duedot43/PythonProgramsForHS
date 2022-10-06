import socket, json

uname = input("Username: ")
serverAddrPort = ("127.0.0.1", 20001)
bufferSize = 1024
# connecting to hosts
sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
def send(msg):
    global serverAddrPort, bufferSize, sock
    if (type(msg) == dict):
        msg = json.dumps(msg)
    else:
        msg = str(msg)
    print(msg)
    sock.sendto(str.encode(msg), serverAddrPort)
    reciv = sock.recvfrom(bufferSize)
    return reciv[0].decode()
out = send({"method": "login", "uname": uname})
print(out)
