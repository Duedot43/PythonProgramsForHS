white = ['a8', 'c8', 'e8', 'g8', 'b7', 'd7', 'f7', 'h7', 'a6', 'c6', 'e6', 'g6', 'b5', 'd5', 'f5', 'h5', 'a4', 'c4', 'e4', 'g4', 'b3', 'd3', 'f3', 'h3', 'a2', 'c2', 'e2', 'g2', 'b1', 'd1', 'f1', 'h1'];
black = ['b8', 'd8', 'f8', 'h8', 'a7', 'c7', 'e7', 'g7', 'b6', 'd6', 'f6', 'h6', 'a5', 'c5', 'e5', 'g5', 'b4', 'd4', 'f4', 'h4', 'a3', 'c3', 'e3', 'g3', 'b2', 'd2', 'f2', 'h2', 'a1', 'c1', 'e1', 'g1'];
input1 = str(input("What position is it?\n"));

if any(ext in input1 for ext in white):
    print("white")
    exit()
if any(ext in input1 for ext in black):
    print("black")
    exit()
print("Fail")
