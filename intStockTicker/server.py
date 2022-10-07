import socket, json, multiprocessing, random, re, boards, turtle, time
import tkinter as Tk
ip = "127.0.0.1"
port = 20001
bufferSize = 16000

def board(ip, bufferSize, port):
    global turtles
    time.sleep(1)
    # connecting to hosts
    sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
    serverAddrPort = (ip, port)

    def rollDice(sock, serverAddrPort, bufferSize, amnt = 1):
        for x in range(amnt):
            dice = []
            random.seed(random.randint(111111111111, 999999999999))
            dice.append(random.choice(["gold", "silver", "bonds", "oil", "industry", "grain"]))
            random.seed(random.randint(111111111111, 999999999999))
            dice.append(random.randint(1, 3))
            random.seed(random.randint(111111111111, 999999999999))
            dice.append(random.choice([0.05, 0.10, 0.20]))
            board = getBoard(sock, serverAddrPort, bufferSize)
            msg = {"method": "move", "amount": dice[2], "stock": dice[0], "direction": dice[1]}
            #msg = {"method": "move", "amount": .10, "stock": "grain", "direction": 1}
            sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
            sock.recvfrom(bufferSize)
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
        print(reciv[0].decode())
        return json.loads(reciv[0].decode())
    def sendChat(sock, serverAddrPort, bufferSize, msg, uname):
        sock.sendto(str.encode(json.dumps({"method": "chat", "msg" : msg, "uname": uname})), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    def privateChat(sock, serverAddrPort, bufferSize, msg, uname, sendTo):
        sock.sendto(str.encode(json.dumps({"method": "private_chat", "msg" : msg, "uname": uname, "user": sendTo})), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    def buy(sock, serverAddrPort, bufferSize, uname, stock, amount):
        msg = {"method": "buy", "uname": uname, "stock": uname, "amount": amount}
        sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    def decodeConsole(sock, serverAddrPort, bufferSize, allowedCat):
        console = getConsole(sock, serverAddrPort, bufferSize)
        realConsole = ""
        for x in console:
            if (x["category"] in allowedCat):
                realConsole += x["msg"] + "\n"
        return realConsole
    def readLocalConsole(inpt, sock, serverAddrPort, bufferSize, uname):
        inputLst = inpt.split(" ")
        command = inputLst[0]
        args = re.findall('(?:[^\s,"]|"(?:\\.|[^"])*")+', inpt.strip(command + " "))
        if (command == "chat"):
            try:
                sendChat(sock, serverAddrPort, bufferSize, args[0].strip('"'), uname)
            except:
                privateChat(sock, serverAddrPort, bufferSize, "Invalid chat message!", "Server", uname)
        elif (command == "roll_dice"):
            try:
                rollDice(sock, serverAddrPort, bufferSize, int(args[0]))
            except:
                rollDice(sock, serverAddrPort, bufferSize)
        elif (command == "buy"):
            buy(sock, serverAddrPort, bufferSize, uname, args[0], int(args[1]))
        elif (command == "refresh"):
            pass
    root = Tk.Tk()
    root.geometry("250x600")
    root.title("Console")

    def Take_input():
        INPUT = consoleBox.get("1.0", "end-1c")
        readLocalConsole(INPUT, sock, serverAddrPort, bufferSize, "Master Console")
        console = decodeConsole(sock, serverAddrPort, bufferSize, ['debug', 'chat', "Master Console"])
        consoleTk.replace('1.0', 'end', console)
        consoleBox.delete("1.0", "end")
        
        
        
    consoleTk = Tk.Text(root, height = 30,
                    width = 25
                    )
    #consoleTk.config(state="disabled")
    consoleBox = Tk.Text(root, height = 1,
                    width = 25
                    )

    Display = Tk.Button(root, height = 1,
                    width = 5,
                    text ="Show",
                    command = lambda:Take_input())

    consoleTk.pack()
    consoleBox.pack()
    Display.pack()

    root.mainloop()



def handleClient():
    localIP = "127.0.0.1"
    localPort = 20001
    bufferSize = 1024
    wn = turtle.Screen()
    wn.bgcolor("#2b2c2b")
    wn.tracer(0)
    boards.drawBoard()
    boards.drawPrices()
    turtles = boards.placeMarkers()
    wn.tracer(1)
    UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    print("UDP server up and listening")

    console = []

    globalDct = {'misc': {}, 'users': {}, 'dice': {}, 'stocks': {"gold": 1.00, 'silver': 1.00, 'bonds': 1.00, 'oil': 1.00, 'industry': 1.00, 'grain': 1.00}}
    #listening for clients and such
    while(True):
        msg, addr1 = UDPServerSocket.recvfrom(bufferSize)
        msg = msg.decode()
        msg = json.loads(msg)
        if (msg["method"] == "login"):
            globalDct['users'][msg['uname']] = {"money": 5000, "shares": {}}
            console.append({"msg": msg['uname'] + " has logged in!", "category": "login"})
            print(msg['uname'] + " has logged in!")
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct['users'][msg['uname']])), addr1)

        elif (msg["method"] == "board"):
            console.append({"msg": "Board requested", "category": "debug"})
            print("Board requested")
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)

        elif (msg["method"] == "set"):
            # type is stocks, users, dice key is the key in that thing in globalDict and value is the value of said thing
            globalDct[msg['type']][msg['key']] = msg['value']
            console.append({"msg": "Values changed! type:" + msg['type'] + " key:" + msg['key'] + " value:" + str(msg['value']), "category": "debug"})
            print("Values changed! type:" + msg['type'] + " key:" + msg['key'] + " value:" + str(msg['value']))
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)

        elif (msg["method"] == "console"):
            if (len(console) - 1 >= 55):
                console = console[len(console) - 1:50]
            console.append({"msg": "Console requested", "category": "debug"})
            print("Console requested")
            UDPServerSocket.sendto(str.encode(json.dumps(console)), addr1)

        elif (msg["method"] == "chat"):
            console.append({"msg": msg['uname'] + "> " + msg['msg'], "category": "chat"})
            print(msg['uname'] + "> " + msg['msg'])
            UDPServerSocket.sendto(str.encode(json.dumps(console)), addr1)

        elif (msg["method"] == "buy"):
            #buying a stock
            globalDct['users'][msg['uname']]['shares'][msg['stock']] = msg['amount']
            globalDct['users'][msg['uname']]['money'] -= msg['amount']
            console.append({"msg": msg['uname'] + " has bought " + str(msg['amount']) + " shares of " + msg['stock'], "category": "activity"})
            print(msg['uname'] + " has bought " + str(msg['amount']) + " shares of " + msg['stock'])
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)

        elif (msg["method"] == "sell"):
            #selling a stock
            globalDct['users'][msg['uname']]['shares'][msg['stock']] = 0
            globalDct['users'][msg['uname']]['money'] += msg['amount']
            console.append({"msg": msg['uname'] + " has sold " + str(msg['amount']) + " shares of " + msg['stock'], "category": "activity"})
            print(msg['uname'] + " has sold " + str(msg['amount']) + " shares of " + msg['stock'])
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)

        elif (msg["method"] == "move"):
            #moving a turtle
            #boards.movePiece(int(msg['amount']), turtles[msg['stock']], int(msg['direction']))
            if int(msg['direction']) == 1:
                turtles[msg['stock']].forward(20 * (int(msg['amount'] * 100)/5))
            else:
                turtles[msg['stock']].backward(20 * (int(msg['amount'] * 100)/5))
            console.append({"msg": msg['stock'] + " has moved " + str(msg['amount']), "category": "debug"})
            print(msg['stock'] + " has moved " + str(msg['direction']) + " " + str(msg['amount']))
            UDPServerSocket.sendto(str.encode(json.dumps(globalDct)), addr1)

        elif (msg["method"] == "private_chat"):
            console.append({"msg": msg['uname'] + "> " + msg['msg'], "category": msg['user']})
            print(msg['uname'] + "> " + msg['msg'])
            UDPServerSocket.sendto(str.encode(json.dumps(console)), addr1)

p = multiprocessing.Process(target=handleClient)
brd = multiprocessing.Process(target=board, args=(ip, bufferSize, port))
p.start()
brd.start()
p.join()
brd.join()
