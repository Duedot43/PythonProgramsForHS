import random
def load_game():
    # outpost [ocupied, how_much_loot ,banoculard included]
    #5 bases
    #this is the main list
    memory_be_gone = ["","","","",""]
    outpost = ["","","","",""]
    #base format [ocupied, loot]
    #base 1 is always occupied
    base1 = [1, random.randint(1,5)]
    base2 = [random.randint(0,1), random.randint(1,5)]
    base3 = [random.randint(0,1), random.randint(1,5)]
    base4 = [random.randint(0,1), random.randint(1,5)]
    base5 = [random.randint(0,1), random.randint(1,5)]
    #im making this so ineffecent so i can easly keep track of everything
    outpost[0] = base1
    outpost[1] = base2
    outpost[2] = base3
    outpost[3] = base4
    outpost[4] = base5
    #8 barns 
    barn = ["","","","","","","",""]
    #barn format [loot]
    barn1 = [random.randint(1,10)]
    barn2 = [random.randint(1,10)]
    barn3 = [random.randint(1,10)]
    barn4 = [random.randint(1,10)]
    barn5 = [random.randint(1,10)]
    barn6 = [random.randint(1,10)]
    barn7 = [random.randint(1,10)]
    barn8 = [random.randint(1,10)]
    #again so i can keep track of things
    barn[0] = barn1
    barn[1] = barn2
    barn[2] = barn3
    barn[3] = barn4
    barn[4] = barn5
    barn[5] = barn6
    barn[6] = barn7
    barn[7] = barn8
    #How big the 5 trees in exiestance are
    tree = ["","","","",""]
    #tree format [dead, big]
    tree1 = [random.randint(0,1), random.randint(5,10)]
    tree2 = [random.randint(0,1), random.randint(5,10)]
    tree3 = [random.randint(0,1), random.randint(5,10)]
    tree4 = [random.randint(0,1), random.randint(5,10)]
    tree5 = [random.randint(0,1), random.randint(5,10)]
    #You shush alright?
    tree[0] = tree1
    tree[1] = tree2
    tree[2] = tree3
    tree[3] = tree4
    tree[4] = tree5
    #Price for everything in the outlands
    #bread, corn,wheat, TNT, fresh_water, bow, arrows, banoculars
    price_outland = ["","","","","","","", ""]
    #template [cost, sellable, quant_per_price]
    bread = [random.randint(10,30), 1, 5]
    corn = [random.randint(10,20), 1, 10]
    wheat = [random.randint(5,20), 1, 15]
    tnt = [random.randint(40,50), 0, 2]
    fresh_water = [random.randint(5,10), 0, 5]
    bow = [random.randint(50,60), 0, 1]
    arrows = [random.randint(3,7), 1, 20]
    banoculars = [random.randint(100,150), 0, 1]
    price_outland[0] = bread
    price_outland[1] = corn
    price_outland[2] = wheat
    price_outland[3] = tnt
    price_outland[4] = fresh_water
    price_outland[5] = bow
    price_outland[6] = arrows
    price_outland[7] = banoculars
    #Price for everything in the city
    #template [cost, sellable, quant_per_prce]
    price_city = ["","","","","","","", ""]
    bread = [random.randint(5,25), 1, 5]
    corn = [random.randint(5,10), 1, 10]
    wheat = [random.randint(5,15), 1, 15]
    tnt = [random.randint(30,45), 0, 2]
    fresh_water = [random.randint(1,3), 0, 5]
    bow = [random.randint(5,30), 0, 1]
    arrows = [random.randint(2,5), 1, 20]
    banoculars = [random.randint(40,50), 0, 1]
    price_city[0] = bread
    price_city[1] = corn
    price_city[2] = wheat
    price_city[3] = tnt
    price_city[4] = fresh_water
    price_city[5] = bow
    price_city[6] = arrows
    price_city[7] = banoculars
    memory_be_gone[0] = outpost
    memory_be_gone[1] = barn
    memory_be_gone[2] = tree
    memory_be_gone[3] = price_outland
    memory_be_gone[4] = price_city
    return memory_be_gone
def load_player_info():
    cpos = [26]
    #[bread,corn,wheat,tnt,fresh_water,bow,arrows,banoculars,money]
    inventory = [0,0,0,0,0,0,0,0,80]
    player = [cpos,inventory]
    return player
