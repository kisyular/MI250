import random

def flipCoin():
    result = random.randrange(2)
    if result == 0:
        return("Heads")
    else: 
        return("Tails")


def casino( dollars):
    flips = 0
    headcount = 0
    casino = 0
    while flips < 300 and dollars > 1:
        dollars = dollars -1
        casino += 1
        result = flipCoin()
        if result=="Heads":
            headcount += 1
            dollars +=1.20
            flips +=1
    return ( [casino,  flips, headcount])


