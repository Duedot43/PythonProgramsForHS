import socket, json, multiprocessing, random, re, time

import tkinter as Tk


ip = str(input("IP: "))
port = int(input("Port: "))
bufferSize = 16000


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
    return json.loads(reciv[0].decode())
def sendChat(sock, serverAddrPort, bufferSize, msg):
    global uname
    sock.sendto(str.encode(json.dumps({"method": "chat", "msg" : msg, "uname": uname})), serverAddrPort)
    reciv = sock.recvfrom(bufferSize)
    return json.loads(reciv[0].decode())
def privateChat(sock, serverAddrPort, bufferSize, msg, sendTo):
    global uname
    sock.sendto(str.encode(json.dumps({"method": "private_chat", "msg" : msg, "uname": uname, "user": sendTo})), serverAddrPort)
    reciv = sock.recvfrom(bufferSize)
    return json.loads(reciv[0].decode())
def buy(sock, serverAddrPort, bufferSize, stock, amount):
    global uname
    if (stock in ["gold", "silver", "bonds", "oil", "industry", "grain"] == False):
        privateChat(sock, serverAddrPort, bufferSize, "Thats not a valid stock!", "Server")
    if (amount%500 == 0):
        msg = {"method": "buy", "uname": uname, "stock": stock, "amount": amount}
        sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    else:
        privateChat(sock, serverAddrPort, bufferSize, "You can only buy in increments of 500", "Server")
def sell(sock, serverAddrPort, bufferSize, stock, amount):
    global uname
    if (stock in ["gold", "silver", "bonds", "oil", "industry", "grain"] == False):
        privateChat(sock, serverAddrPort, bufferSize, "Thats not a valid stock!", "Server")
    if (amount%500 == 0):
        msg = {"method": "sell", "uname": uname, "stock": stock, "amount": amount}
        sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
        reciv = sock.recvfrom(bufferSize)
        return json.loads(reciv[0].decode())
    else:
        privateChat(sock, serverAddrPort, bufferSize, "You can only sell in increments of 500", "Server")
def decodeConsole(sock, serverAddrPort, bufferSize, allowedCat):
    console = getConsole(sock, serverAddrPort, bufferSize)
    realConsole = ""
    for x in console:
        if (x["category"] in allowedCat):
            realConsole += x["msg"] + "\n"
    return realConsole
def help(sock, serverAddrPort, bufferSize):
    global uname
    msg = {"method": "private_chat", "msg" : """
    'chat'
    Args:
        <message> Message you with to send in double quotes.
        
    'roll_dice' Rolls the dice and moves the board.
    Args:
        <rolls> Times to roll the dice.

    'buy' Buys a stock.
    Args:
        <stock> Can be 1 of 6 gold, silver, bonds, oil, industry, or grain.
        <ammount> Must be a multipul of 500.
        
    'sell' Sells a stock.
    Args:
        <stock> Can be 1 of 6 gold, silver, bonds, oil, industry, or grain.
        <ammount> Must be a multipul of 500.
        
    'refresh'
        Refreshes the console window
        
    'view_stocks '
        Views your money and stocks.

    'help'
        Shows this message.
    
    'login' Logs you in to the server.
    Args:
        <username> Username you wish to use.

    'private_chat' Sends a private message to a user.
    Args:
        <msg> Message you wish to send in double quotes.
        <user> Username of the user you wish to send the message to in double quotes.
    """, 
            
    "uname": "Server", "user": uname}
    sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
    reciv = sock.recvfrom(bufferSize)
    return json.loads(reciv[0].decode())
def getUserStocks(sock, serverAddrPort, bufferSize):
    global uname
    user = getBoard(sock, serverAddrPort, bufferSize)['users'][uname]
    privateChat(sock, serverAddrPort, bufferSize, "Money: " + str(user['money']) + "\nGold: " + str(user['shares']['gold']) + "\nSilver: " + str(user['shares']['silver']) + "\nBonds: " + str(user['shares']['bonds']) + "\nOil: " + str(user['shares']['oil']) + "\nIndustry: " + str(user['shares']['industry']) + "\nGrain: " + str(user['shares']['grain']), uname)
def login(sock, serverAddrPort, bufferSize, uname):
    msg = {"method": "login", "uname": uname}
    sock.sendto(str.encode(json.dumps(msg)), serverAddrPort)
    reciv = sock.recvfrom(bufferSize)
    return json.loads(reciv[0].decode())
def readLocalConsole(inpt, sock, serverAddrPort, bufferSize):
    global uname
    inputLst = inpt.strip("\n").lower().split(" ")
    command = inputLst[0]
    args = re.findall('(?:[^\s,"]|"(?:\\.|[^"])*")+', inpt.strip(command + " ").strip("\n"))
    if (command == "chat"):
        try:
            sendChat(sock, serverAddrPort, bufferSize, args[0].strip('"'))
        except:
            privateChat(sock, serverAddrPort, bufferSize, "Invalid chat message!", "Server")
    elif (command == "private_chat"):
        try:
            privateChat(sock, serverAddrPort, bufferSize, args[1].strip('"'), args[0].strip('"'))
        except:
            privateChat(sock, serverAddrPort, bufferSize, "Invalid private chat message!", "Server")
    elif (command == "roll_dice"):
        try:
            rollDice(sock, serverAddrPort, bufferSize, int(args[0]))
        except:
            rollDice(sock, serverAddrPort, bufferSize)
    elif (command == "buy"):
        try:
            buy(sock, serverAddrPort, bufferSize, args[0], int(args[1]))
        except:
            print("You are not logged in!")
    elif (command == "sell"):
        try:
            sell(sock, serverAddrPort, bufferSize, args[0], int(args[1]))
        except:
            print("You are not logged in!")
    elif (command == "refresh"):
        pass
    elif (command == "help"):
        help(sock, serverAddrPort, bufferSize)
    elif (command == "view_stocks"):
        try:
            getUserStocks(sock, serverAddrPort, bufferSize)
        except:
            print("You are not logged in!")
    elif (command == "login"):
        try:
            login(sock, serverAddrPort, bufferSize, args[0])
            uname = args[0]
        except:
            print("Invalid username!")
    else:
        print("Invalid command!")
root = Tk.Tk()
root.geometry("800x600")
root.title("Console")

def Take_input():
    INPUT = consoleBox.get("1.0", "end-1c")
    
    readLocalConsole(INPUT, sock, serverAddrPort, bufferSize)
    console = decodeConsole(sock, serverAddrPort, bufferSize, ['chat', "activity", uname, "login"])
    consoleTk.replace('1.0', 'end', console)
    consoleBox.delete("1.0", "end")
    
    
    
consoleTk = Tk.Text(root, height = 30,
                width = 100
                )
#consoleTk.config(state="disabled")
consoleBox = Tk.Text(root, height = 1,
                width = 25
                )

Display = Tk.Button(root, height = 1,
                width = 5,
                text ="Show",
                command = lambda:Take_input())
root.bind('<Return>', lambda event: Take_input())
consoleTk.pack()
consoleBox.pack()
Display.pack()

root.mainloop()