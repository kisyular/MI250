import gamble
def eveningAtCasino(gamblers):
    totalFlips = 0
    totalHead = 0
    totalCasino = 0
    for g in gamblers:
        lst = gamble.casino(g)
        totalFlips +=int(lst[1])
        totalCasino +=int(lst[0])
        totalHead +=int(lst[2])
    return(totalFlips, totalHead, totalCasino)

gamblers = [10, 10, 10]
print(eveningAtCasino(gamblers))

