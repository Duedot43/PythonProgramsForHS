import random,os,time,get
#unlocked locations
def desc(plr_list, var_list):
    pos = get.pos(plr_list)
    if pos == 1:
        pier(plr_list, var_list)
    if pos == 2 or pos == 5 or pos == 10 or pos == 23 or pos == 24 or pos == 25 or pos == 27:
        barn(plr_list, var_list)
    if pos == 3 or pos == 4 or pos == 7 or pos == 9 or pos == 22:
        outpost(plr_list, var_list)
    if pos == 26:
        spawn(plr_list, var_list)
    if pos == 1:
        pier(plr_list, var_list)
    if pos == 17:
        forest(plr_list, var_list)
    if pos == 28:
        outlaw(plr_list, var_list)
    if pos == 6:
        vinyard(plr_list, var_list)
    if pos == 29:
        milbase(plr_list, var_list)
    if pos == 21:
        river(plr_list, var_list)
    if pos == 18:
        mineshaft(plr_list, var_list)
    if pos == 16 or pos ==  15 or pos ==11:
        gate(plr_list, var_list)
def spawn(plr_list, var_list):
    print("You wake up in a ditch, with farms surrounding you. You can feel a note inside of your pocket.")
def outpost(plr_list, var_list):
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
def barn(plr_list, var_list):
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
def pier(plr_list, var_list):
    pierrand = random.randint(1,3)
    if pierrand == 1:
        print("You find a pier, it sticks out from the surrounding coast.")
    elif pierrand == 2:
        print("You walk onto a pier, it seems as if a fishermans paradise.")
    elif pierrand == 3:
        print("You see a pier, the sight of food makes you hungry.")
def forest(plr_list, var_list):
    forestrand = random.randint(1,3)
    if forestrand == 1:
        print("You find a forest, trees consume your eyesight.")
    elif forestrand == 2:
        print("You run into a forest, all you can see is trees for miles.")
    elif forestrand == 3:
        print("You wander into a forest, quickly getting lost in its trees.")
def outlaw(plr_list, var_list):
    outloowrand = random.randint(1,3)
    if outloowrand == 1:
        print("You find an outpost through a clearing, bandits seem to inhabit it.")
    elif outloowrand == 2:
        print("You exit the forest to a band of outlaws, they seem to inhabit a village nearby.")
    elif outloowrand == 3:
        print("You exit the forest to a outpost, no guard could ever get here.")
def vinyard():
    vinyardrand = random.randint(1,3)
    if vinyardrand == 1:
        print("You enter a vinyard, the smell of grapes is powerful.")
    elif vinyardrand == 2:
        print("You enter a vinyard, it is surrounded riches.")
    elif vinyardrand == 3:
        print("You enter a vinyard, nights of fun must have happened here before.")
def milbase(plr_list, var_list):
    milbaserand = random.randint(1,3)
    if milbaserand == 1:
        print("You come across a Military Base, the heart of the army.")
    elif milbaserand == 2:
        print("You walk into a Military Base, ready for war as ever.")
    elif milbaserand == 3:
        print("You wander into a Military Base, there is hundreds of pieces of gear.")
def river(plr_list, var_list):
    print("You come upon a river, the tide takes anything it can.")
def mineshaft(plr_list, var_list):
    print("You walk to the entrance of a mineshaft, it has been boarded up for years.")
def gate(plr_list, var_list):
    print("You walk into the gate to the city, it hangs suspended from above.")
#locked locationss
