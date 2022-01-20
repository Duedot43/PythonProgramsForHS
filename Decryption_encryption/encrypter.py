import shifty
import decrypter
msg1 = str(input("What is the message you would like to encrypt?\n"))

msg = shifty.find(msg1)

msgstr = shifty.Convert(msg)
msgenc = shifty.encrypt(msgstr)
msgencstr = shifty.stringlist(msgenc)
print ("Here is your message encrypted...\n", msgencstr)

print("Here is your message decrypted...")
decrypter.decrypt(msgenc)
