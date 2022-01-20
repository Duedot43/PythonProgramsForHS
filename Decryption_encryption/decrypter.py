import shifty
def decrypt(msgenc):
    decryptmsg = shifty.decrypt(msgenc)
    string = shifty.stringlist(decryptmsg)
    print (string)
    