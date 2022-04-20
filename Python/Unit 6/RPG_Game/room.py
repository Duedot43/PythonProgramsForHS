import random,os,time,get
#unlocked locations
def desc(plr_list, var_list):
    pos = get.pos(plr_list)
    if pos == 26:
        spawn(plr_list, var_list)
def spawn(plr_list, var_list):
    print("You wake up in a ditch, with farms surrounding you. You can feel a note inside of your pocket.")
def outpost():
    outpostrand = random.randint(1,6)
    if outpostrand == 1:
        print("You wander into an outpost, it is filled with weapons and tools of war.")
    elif outpostrand == 2:
        print("You walk into an outpost, the eerie feeling makes you tingle.")
    elif outpostrand == 3:
        print("You sneak into an outpost, you wonder how soldiers survive in them.")
    elif outpostrand == 4:
        print("Whilst walking you happen upon an outpost, it sits as a tall tower above the land.")
    elif outpostrand == 5:
        print("You come across an outpost, it seems as if it is ready for war.")
    elif outpostrand == 6:
        print("You find an outpost, maybe the tools it holds could be of use.")
def barn():
    barnrand = random.randint(1,5)
    if barnrand == 1:
        print("You discover a barn, the animals seem delighted to see sunlight.")
    elif barnrand == 2:
        print("You wander into a barn, the smell of hay overwhelms you.")
    elif barnrand == 3:
        print("You happen upon a barn, it is painted a velvet red.")
    elif barnrand == 4:
        print("You find a barn, it looks greatly used.")
    elif barnrand == 5:
        print("You exit a field to a barn, the sound of life calms you.")
def pier():
    pierrand = random.randint(1,3)
    if pierrand == 1:
        print("You find a pier, it sticks out from the surrounding coast.")
    elif pierrand == 2:
        print("You walk onto a pier, it seems as if a fishermans paradise.")
    elif pierrand == 3:
        print("You see a pier, the sight of food makes you hungry.")
def forest():
    forestrand = random.randint(1,3)
    if forestrand == 1:
        print("You find a forest, trees consume your eyesight.")
    elif forestrand == 2:
        print("You run into a forest, all you can see is trees for miles.")
    elif forestrand == 3:
        print("You wander into a forest, quickly getting lost in its trees.")
def outlaw():
    pass
def vinyard():
    pass
def milbase():
    pass
def river():
    pass
def mineshaft():
    pass
#locked locationss
