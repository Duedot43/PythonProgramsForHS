def disp(cpos):
    #we have 28 Total rooms.
    if cpos == 1:
        print("You are at the pier\nTo the northeast is a barn\nTo the east there is a military outpost")
        ava = [["northeast", 2], ["east", 7]]
        return ava
    if cpos == 2:
        print("You are at a barn\nTo the south there is a military outpost\nTo the east there is a military outpost\nTo the west is the pier")
        ava = [["south", 7], ["east", 3], ["west", 1]]
        return ava
    if cpos == 3:
        print("You are at a military outpost\nTo the east there is the military base\nTo the west there is a barn")
        ava = [["east", 29], ["west", 2]]
        return ava
    if cpos == 29:
        print("You are at the military base\nTo the south of you is the city\nTo the southeast of you is a military outpost\nTo the west of you is a military outpost")
        ava = [["southeast", 4], ["west", 3]]
        return ava
    if cpos == 4:
        print("You are at a military outpost\n To the northeast of you is a barn\nTo the northwest of you is the military base")
        ava = [["northeast", 5], ["northwest", 29]]
        return ava
    if cpos == 5:
        print("You are at a barn\nTo the east of you is a mountan village\nTo the southeast of you is a millitary outpost\nTo the west of you is a military outpost")
        ava = [["east", 6], ["southeast", 9], ["west", 4]]
        return ava
    if cpos == 6:
        print("You are at a mountan village you can buy things here\nTo the southeast of you is a military outpost\nTo the west of you is a barn")
        ava = [["southeast", 9], ["west", 5]]
        return ava
    if cpos == 7:
        print("You are at a military base\nTo the north of you is a barn\nTo the west of you is the pier\nTo the south of you is the cave")
        ava = [["north", 2], ["west", 1],["south", 11]]
        return ava
    if cpos == 8:
        print("You are in the military district of the city\nTo the south of you looms the castle\nTo the southwest of you is the commerce district\nTo the southeast of you is the housing district")
        ava = [["south", 13], ["southwest", 12], ["southeast", 14]]
        return ava
    if cpos == 9:
        print("You are at a military outpost\nTo the northwest there is a barn\nTo the south of you is the forrest\nTo the southwest of you is the east gate")
        ava = [["northwest", 5], ["south", 17], ["southwest", 16]]
        return ava