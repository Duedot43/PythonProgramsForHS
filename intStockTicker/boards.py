import turtle, time

def placeMarkers():
  global turtles
  turtles = {'gold': {"color": "yellow", "chords": [125, 10]}, 'silver': {"color": "silver", "chords": [75, 10]}, 'oil': {"color": "orange", "chords": [25, 10]}, 'bonds': {"color": "green", "chords": [-25, 10]}, 'industry': {"color": "brown", "chords": [-75, 10]}, 'grain': {"color": "blue", "chords": [-125, 10]}}

  for stock in enumerate(turtles):
    tur = turtle.Turtle()
    tur.shape('circle')
    tur.color(turtles[stock[1]]['color'])
    tur.penup()
    tur.goto(turtles[stock[1]]['chords'][0], turtles[stock[1]]['chords'][1])
    tur.left(90)
    turtles[stock[1]] = tur
    tur = ""
  return turtles






def drawBoard():
  #wn.tracer(0)
  draw = turtle.Turtle()
  draw.speed(10)
  draw.hideturtle()
  draw.color('white')
  draw.penup()
  draw.goto(-150,-400)
  draw.pendown()
  #wn.tracer(0)
  for i in range(0, 41):
    draw.forward(300)
    draw.left(90)
    draw.forward(20)
    draw.left(90)
    for i in range(0, 3):
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
  print("draw prices")
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

def movePiece(ammnt, turtleId, direction):
  if direction == 1:
    turtleId.forward(20 * (ammnt/5))
  else:
    turtleId.backward(20 * (ammnt/5))
#drawBoard()
#drawPrices()
#turtles = placeMarkers()
#time.sleep(10)