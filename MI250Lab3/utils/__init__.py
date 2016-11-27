import random
import decimal
import numpy as np

def generator(dictn, times):
    sentence = '' # Initialize an empty string called sentence
    listValue = [] # Empty list for storing dictionary values
    listKeys = [] # Empty list for storing dictionary keys
    revertedDictn = {} # Here we will reverse the dictionary so keys are values and values are keys
    
    # Reverse the dictionary
    for k, v in dictn.items():
        listValue.append(v)
        listKeys.append(v)
        revertedDictn[v] = k
        
    # Here we will construct a random string by assigning it a different probabilities of character occurence
    for i in range (50):
        a =np.random.choice(listKeys, p=listValue)
        sentence +=revertedDictn[a]
    return(sentence)
generator ({"a":.1,"b":.3,"c":.6}, 50)


def compressor(s):
    characters= [] # Here we will store all the characters found in the string
    finalCompressed = '' # This will be the final compressed string with both the numbers and the letters
    
    # Append each letter in the characters
    for i in s:
        if i not in characters:
            characters.append(i)
    letterDictn ={}
    
    # Now we will count how many times the character is in the string
    for letter in characters:
        appearance =(s).count(letter)
        appearance =  round(appearance, 2)
        letterDictn[letter] = appearance
        
    # Finally we will join the string together to make a compressed version
    for k, v in letterDictn.items():
        finalCompressed +=str(k)+str(v)
    return(finalCompressed)
compressor('aaaaaaabaaaaaacaaaaaaaaaaaaaaaaaaabaaaaaaaabaabacakkkkkkddddddyyy') 


def decompressed(s):
    getLetters= list(s)
    splitters = []
    for letter in getLetters:
        if letter.isalpha():
            splitters.append(letter)
    for char in splitters:
        s=s.replace(char,' ')  
    numbersList = s.split()
    #print(numbersList, splitters)
    joinedString = ''
    for i in range (len(splitters)):
        joinedString +=splitters[i]*int(numbersList[i])
    joinedString = ''.join(random.sample(joinedString,len(joinedString)))
    return(joinedString)
string = "y3c2b4k6d6a44"
decompressed(string)
