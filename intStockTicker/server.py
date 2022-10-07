import socket, json, multiprocessing, random, re, boards, turtle
ip = "127.0.0.1"
port = 20001
bufferSize = 1024
wn = turtle.Screen()
wn.bgcolor("grey")
wn.tracer(0)
boards.drawBoard()
boards.drawPrices()
turtles = boards.placeMarkers()
wn.tracer(1)
def board(ip, bufferSize, port):
    global turtles
    # connecting to hosts
    sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
    serverAddrPort = (ip, port)

    def rollDice():
        dice = []
        random.seed(random.randint(111111111111, 999999999999))
        dice.append(random.choice(["gold", "silver", "bonds", "oil", "industrials", "grain"]))
        random.seed(random.randint(111111111111, 999999999999))
        dice.append(random.randint(1, 3))
        random.seed(random.randint(111111111111, 999999999999))
        dice.append(random.choice([0.05, 0.10, 0.20]))
        return dice
    def getBoard(sock, serverAddrPort, bufferSize):
        msg = {"method": "board"}
        sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    def set(sock, serverAddrPort, bufferSize, msg):
        sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    def getConsole(sock, serverAddrPort, bufferSize):
        msg = {"method": "console"}
        sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    def sendChat(sock, serverAddrPort, bufferSize, msg, uname):
        sock.sendto(str.encode(json.dumps({"method": "chat", "msg" : msg, "uname": uname})), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    def buy(sock, serverAddrPort, bufferSize, uname, stock, amount):
        msg = {"method": "buy", "uname": uname, "stock": uname, "amount": amount}
        sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    def readLocalConsole(inpt, sock, serverAddrPort, bufferSize, uname):
        inputLst = inpt.split(" ")
        command = inputLst[0]
        args = re.findall('(?:[^\s,"]|"(?:\\.|[^"])*")+', inpt.strip(command + " "))
        if (command == "chat"):
            sendChat(sock, serverAddrPort, bufferSize, args[0].strip('"'), uname)
        elif (command == "roll_dice"):
            dice = rollDice()
            set(sock, serverAddrPort, bufferSize, {"method": "set", "type": "dice", "key": "0", "value": dice})
        elif (command == "buy"):
            buy(sock, serverAddrPort, bufferSize, uname, args[0], int(args[1]))
    readLocalConsole('roll_dice', sock, serverAddrPort, bufferSize, "test")
    board = getBoard(sock, serverAddrPort, bufferSize)


def handleClient():
    global turtles
    localIP = "127.0.0.1"
    localPort = 20001
    bufferSize = 1024

    UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    print("UDP server up and listening")

    console = []

    globalDct = {'misc': {}, 'users': {}, 'dice': {}, 'stocks': {"gold": 1.00, 'silver': 1.00, 'bonds': 1.00, 'oil': 1.00, 'industrials': 1.00, 'grain': 1.00}}

    #listening for clients and such
    while(True):
        msg, addr1 = UDPServerSocket.recvfrom(bufferSize)
        msg = msg.decode()
        msg = json.loads(msg)
        if (msg["method"] == "login"):
            globalDct['users'][msg['uname']] = {"money": 5000, "shares": {}}
            console.append({"msg": msg['uname'] + " has logged in!", "catagory": "login"})
            print(msg['uname'] + " has logged in!")
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct['users'][msg['uname']])), addr1)

        elif (msg["method"] == "board"):
            console.append({"msg": "Board requested", "catagory": "debug"})
            print("Board requested")
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)

        elif (msg["method"] == "set"):
            # type is stocks, users, dice key is the key in that thing in globalDict and value is the value of said thing
            globalDct[msg['type']][msg['key']] = msg['value']
            console.append({"msg": "Values changed! type:" + msg['type'] + " key:" + msg['key'] + " value:" + str(msg['value']), "catagory": "debug"})
            print("Values changed! type:" + msg['type'] + " key:" + msg['key'] + " value:" + str(msg['value']))
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)

        elif (msg["method"] == "console"):
            console.append({"msg": "Console requested", "catagory": "debug"})
            print("Console requested")
            UDPServerSocket.sendto(str.encode(json.dumps(console)), addr1)

        elif (msg["method"] == "chat"):
            console.append({"msg": msg['uname'] + "> " + msg['msg'], "catagory": "chat"})
            print(msg['uname'] + "> " + msg['msg'])
            UDPServerSocket.sendto(str.encode(json.dumps(console)), addr1)

        elif (msg["method"] == "buy"):
            #buying a stock
            globalDct['users'][msg['uname']]['shares'][msg['stock']] = msg['amount']
            globalDct['users'][msg['uname']]['money'] -= msg['amount']
            console.append({"msg": msg['uname'] + " has bought " + str(msg['amount']) + " shares of " + msg['stock'], "catagory": "activity"})
            print(msg['uname'] + " has bought " + str(msg['amount']) + " shares of " + msg['stock'])
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)

        elif (msg["method"] == "sell"):
            #selling a stock
            globalDct['users'][msg['uname']]['shares'][msg['stock']] = 0
            globalDct['users'][msg['uname']]['money'] += msg['amount']
            console.append({"msg": msg['uname'] + " has sold " + str(msg['amount']) + " shares of " + msg['stock'], "catagory": "activity"})
            print(msg['uname'] + " has sold " + str(msg['amount']) + " shares of " + msg['stock'])
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)

        elif (msg["method"] == "move"):
            #moving a turtle
            boards.movePiece(msg['amount'], turtles[msg['stock']], msg['direction'])
            console.append({"msg": msg['stock'] + " has moved " + str(msg['amount']), "catagory": "debug"})
            print(msg['stock'] + " has moved " + str(msg['amount']))
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)
p = multiprocessing.Process(target=handleClient)
brd = multiprocessing.Process(target=board, args=(ip, bufferSize, port))
p.start()
brd.start()
p.join()
brd.join()