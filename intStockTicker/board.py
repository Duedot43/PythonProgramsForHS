import turtle


def placeMarkers():
  global goldTurtle,silverTurtle,oilTurtle,bondsTurtle,industryTurtle,grainTurtle

  goldTurtle = turtle.Turtle()
  goldTurtle.shape('circle')
  goldTurtle.color('yellow')
  goldTurtle.penup()
  goldTurtle.goto(125,10)
  goldTurtle.left(90)

  silverTurtle = turtle.Turtle()
  silverTurtle.shape('circle')
  silverTurtle.color('silver')
  silverTurtle.penup()
  silverTurtle.goto(75,10)
  silverTurtle.left(90)

  oilTurtle = turtle.Turtle()
  oilTurtle.shape('circle')
  oilTurtle.color('orange')
  oilTurtle.penup()
  oilTurtle.goto(25,10)
  oilTurtle.left(90)

  bondsTurtle = turtle.Turtle()
  bondsTurtle.shape('circle')
  bondsTurtle.color('green')
  bondsTurtle.penup()
  bondsTurtle.goto(-25,10)
  bondsTurtle.left(90)

  industryTurtle = turtle.Turtle()
  industryTurtle.shape('circle')
  industryTurtle.color('brown')
  industryTurtle.penup()
  industryTurtle.goto(-75,10)
  industryTurtle.left(90)

  grainTurtle = turtle.Turtle()
  grainTurtle.shape('circle')
  grainTurtle.color('blue')
  grainTurtle.penup()
  grainTurtle.goto(-125,10)
  grainTurtle.left(90)


def movePiece(number,stock, direction):
  global goldTurtle,silverTurtle,oilTurtle,bondsTurtle,industryTurtle,grainTurtle, stockValues
  if stock == "Grain":
    if direction == "up":
      grainTurtle.forward(20 * (number/5))
      stockValues[1] = stockValues[1] + (float(number)/100)
    else:
      grainTurtle.backward(20 * (number/5))
      stockValues[1]= stockValues[1] - (float(number)/100)
      print(stockValues)
  elif stock == "Industry":
    if direction == "up":
      industryTurtle.forward(20 * (number/5))
      stockValues[2] = stockValues[2] + (float(number)/100)
    else:
      industryTurtle.backward(20 * (number/5))
      stockValues[2]= stockValues[2] - (float(number)/100)
  elif stock == "Bonds":
    if direction == "up":
      bondsTurtle.forward(20 * (number/5))
      stockValues[3] = stockValues[3] + (float(number)/100)
    else:
      bondsTurtle.backward(20 * (number/5))
      stockValues[3]= stockValues[3] - (float(number)/100)
  elif stock == "Oil":
    if direction == "up":
      oilTurtle.forward(20 * (number/5))
      stockValues[4] = stockValues[4] + (float(number)/100)
    else:
      oilTurtle.backward(20 * (number/5))
      stockValues[4]= stockValues[4] - (float(number)/100)
  elif stock == "Silver":
    if direction == "up":
      silverTurtle.forward(20 * (number/5))
      stockValues[5] = stockValues[5] + (float(number)/100)
    else:
      silverTurtle.backward(20 * (number/5))
      stockValues[5]= stockValues[5] - (float(number)/100)
  elif stock == "Gold":
    if direction == "up":
      goldTurtle.forward(20 * (number/5))
      stockValues[6] = stockValues[6] + (float(number)/100)
    else:
      goldTurtle.backward(20 * (number/5))
      stockValues[6]= stockValues[6] - (float(number)/100)    






def drawBoard():
  print("Drawing board")
  draw = turtle.Turtle()
  draw.hideturtle()
  draw.color('white')
  draw.penup()
  draw.goto(-150,-400)
  draw.pendown()
  #wn.tracer(0)
  for i in range(41):
    draw.forward(300)
    draw.left(90)
    draw.forward(20)
    draw.left(90)
    for i in range(3):
      draw.forward(50)
      draw.left(90)
      draw.forward(20)
      draw.right(90)
      draw.forward(50)
      draw.right(90)
      draw.forward(20)
      draw.left(90)
    draw.right(180)
  draw.forward(300)
  draw.color("light yellow")
  draw.hideturtle()
  draw.penup()
  draw.goto(-150,0)
  #draw.heading(0)
  draw.pendown()
  draw.begin_fill()
  draw.forward(300)
  draw.left(90)
  draw.forward(20)
  draw.left(90)
  draw.forward(300)
  draw.left(90)
  draw.forward(20)
  draw.end_fill()
  #wn.tracer(1)


def drawPrices():
  print("draw pieces")
  pen = turtle.Turtle()
  pen.color("white")
  pen.penup()
  pen.goto(-180, -400)
  pen.left(90)
  price = 0.00
  for i in range(41):
      pen.write(f"${round(price,2)}", align="center", font=('Arial', 12, 'normal'))
      pen.forward(20.1)
      price = price + 0.05
      
  pen.hideturtle()

def movePiece(number,stock, direction):
  global goldTurtle,silverTurtle,oilTurtle,bondsTurtle,industryTurtle,grainTurtle, stockValues
  if stock == "Grain":
    if direction == "up":
      grainTurtle.forward(20 * (number/5))
      stockValues[1] = stockValues[1] + (float(number)/100)
    else:
      grainTurtle.backward(20 * (number/5))
      stockValues[1]= stockValues[1] - (float(number)/100)
      print(stockValues)
  elif stock == "Industry":
    if direction == "up":
      industryTurtle.forward(20 * (number/5))
      stockValues[2] = stockValues[2] + (float(number)/100)
    else:
      industryTurtle.backward(20 * (number/5))
      stockValues[2]= stockValues[2] - (float(number)/100)
  elif stock == "Bonds":
    if direction == "up":
      bondsTurtle.forward(20 * (number/5))
      stockValues[3] = stockValues[3] + (float(number)/100)
    else:
      bondsTurtle.backward(20 * (number/5))
      stockValues[3]= stockValues[3] - (float(number)/100)
  elif stock == "Oil":
    if direction == "up":
      oilTurtle.forward(20 * (number/5))
      stockValues[4] = stockValues[4] + (float(number)/100)
    else:
      oilTurtle.backward(20 * (number/5))
      stockValues[4]= stockValues[4] - (float(number)/100)
  elif stock == "Silver":
    if direction == "up":
      silverTurtle.forward(20 * (number/5))
      stockValues[5] = stockValues[5] + (float(number)/100)
    else:
      silverTurtle.backward(20 * (number/5))
      stockValues[5]= stockValues[5] - (float(number)/100)
  elif stock == "Gold":
    if direction == "up":
      goldTurtle.forward(20 * (number/5))
      stockValues[6] = stockValues[6] + (float(number)/100)
    else:
      goldTurtle.backward(20 * (number/5))
      stockValues[6]= stockValues[6] - (float(number)/100)    
