print("So for context you are poor and only hav $20 in your wallett and you have to realy on your ritch friends who also have $20 in their wallet to pay your bill, and hey why are you leaving a tip for a $50 meal when you only have $20??")
money = float(input("How much money do you owe"));
people = int(input("How many people do you have to split the money (press 1 if you are lonley)"));
tip = str(input("Whats the tip?"));
newtip = "1." + tip
newtip = float(newtip);
totalplstip = money*newtip
print (totalplstip);
totalplstip = float(totalplstip);
poormansshare = totalplstip/people
print("your share is ", poormansshare);
if poormansshare > 20:
    poormanspoorness = poormansshare-20
    print("you are too poor you are $", poormanspoorness, " short")
else:
    print("nice you are just rich enough to survive a expensive meal with your friends")