import get
def outpost(user_list):
    pos = get.pos(user_list)
    if pos == 3 or pos == 4 or pos == 7 or pos == 9 or pos == 22:
        return True
    else:
        return False
def barn(user_list):
    pos = get.pos(user_list)
    if pos == 2 or pos == 5 or pos == 10 or pos == 23 or pos == 24 or pos == 25 or pos == 27:
        return True
    else:
        return False