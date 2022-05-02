import random,os,time,get,at
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
def see(plr_list, var_list, see_what, ava, bob_input):
    #binocular system
    place_thing = get.place(ava, bob_input[1])
    num_pos = get.place(ava, see_what)
    if get.inventory(plr_list, 7) >= 1:
        if num_pos[0] == 1:
            if at.city_raw(get.pos(plr_list)) == False:
                if at.outpost_raw(num_pos[1]):
                    print("You see an outpost in the distance")
                    if get.outpost(0,get.pos2outpost_raw(place_thing[1]),var_list) == 1:
                        print("The outpost is occupied by Guards.")
                        return 0
                    else:
                        print("There are no guards guarding the outpost.")
                        return 0 
                elif at.barn_raw(num_pos[1]):
                    print("You see a barn in the distance")
                    return 0
                elif at.mil_raw(num_pos[1]):
                    print("You see a military base in the distance")
                    return 0
                elif at.gate_raw(num_pos[1]) :
                    print("You cannot see into the city")
                    return 0
                elif at.forest_raw(num_pos[1]) :
                    print("You see a forest in the distance")
                    return 0 
                elif at.river_raw(num_pos[1]) :
                    print("You see a river in the distance")
                    return 0 
                elif at.mineshaft_raw(num_pos[1]) :
                    print("You see a mineshaft in the distance")
                    return 0 
                elif at.outlaw_raw(num_pos[1]) :
                    print("You see a outlaw camp in the distance")
                    return 0 
                elif at.vinyard_raw(num_pos[1]) :
                    print("You see a vinyard in the distance")
                    return 0 
                elif at.pier_raw(num_pos[1]) :
                    print("You see the pier in the distance")
                    return 0 
            else:
                print("You cannot use binoculars in the city.")
                return 0
        else:
            print("Invalid Direction")
            return 0
    else:
        print("You do not have binoculars")
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
    if get.outpost(0,get.pos2outpost(plr_list), var_list) == 1:
        print("The outpost is occupied by soldiers, you must tread lightly.")
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 0:
        print("You see some of the soldiers bread on the table.")
        #bread
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 1:
        print("You see some of the soldiers corn on the table.")
        #corn
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 2:
        print("You see some of the soldiers wheat on the table.")
        #wheat
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 3:
        print("You see some TNT falling out of a closet.")
        #TNT
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 4:
        print("You see some of the soldiers fresh water in a cabinent.")
        #fresh water?
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 5:
        print("You see a soldiers bow hanging on the wall.")
        #bow
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 6:
        print("You see a arrow stash falling out of a bin.")
        #arrows
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 7:
        print("You see some binoculars resting on the ground.")
        #binoculars
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 8:
        print("You find a sword hanging on the wall.")
        #sword
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 9:
        print("You see a spear leaning on the wall.")
        #spear
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 10:
        print("You see a mace leaning on a cabinet.")
        #mace
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 11:
        print("You see a dagger lying on the table.")
        #dagger
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 12:
        print("You see a axe hanging on the wall.")
        #axe
    if get.outpost(1,get.pos2outpost(plr_list), var_list) == 13:
        print("You see some firewood next to a firepit.")
        #wood
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
    if get.barn(get.pos2barn(plr_list), var_list) == 1:
        print("You see some corn on the table.")
        #corn
    if get.barn(get.pos2barn(plr_list), var_list) == 2:
        print("You see some wheat on the table.")
        #wheat
    if get.barn(get.pos2barn(plr_list), var_list) == 3:
        print("You see some TNT falling out of a closet.")
        #TNT
    if get.barn(get.pos2barn(plr_list), var_list) == 4:
        print("You see some fresh water in a cabinent.")
        #fresh water?
    if get.barn(get.pos2barn(plr_list), var_list) == 5:
        print("You see a bow hanging on the wall.")
        #bow
    if get.barn(get.pos2barn(plr_list), var_list) == 6:
        print("You see a arrow stash falling out of a bin.")
        #arrows
    if get.barn(get.pos2barn(plr_list), var_list) == 7:
        print("You see some binoculars resting on the ground.")
        #binoculars
    if get.barn(get.pos2barn(plr_list), var_list) == 8:
        print("You find a sword hanging on the wall.")
        #sword
    if get.barn(get.pos2barn(plr_list), var_list) == 9:
        print("You see a spear leaning on the wall.")
        #spear
    if get.barn(get.pos2barn(plr_list), var_list) == 10:
        print("You see a mace leaning on a cabinet.")
        #mace
    if get.barn(get.pos2barn(plr_list), var_list) == 11:
        print("You see a dagger lying on the table.")
        #dagger
    if get.barn(get.pos2barn(plr_list), var_list) == 12:
        print("You see a axe hanging on the wall.")
        #axe
    if get.barn(get.pos2barn(plr_list), var_list) == 13:
        print("You see some firewood next to a firepit.")
        #wood
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
    pos = get.pos(plr_list)
    if pos == 15 or pos == 11:
        print("You walk into the gate to the city, it hangs suspended from above.")
    if pos == 16:
        print("You are at the outer city gates, it leads to the towering city above")
#locked locationss
