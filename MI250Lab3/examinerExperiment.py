
# Import the Necessary Modules
import utils
import pandas as pd
import json


def experimenter (dictn, length, numberSample):
    finalDictn = {} # After manipulating the dictionary given, this will be output.
    strDictn = str(dictn)+str(length) # to use the dictionary as key to the finalDictn, we have to make it a string
    file = "textfile.json"
    mainDict = {} # here we will store the values we read initially from the file
    mainList = []
    
    #check if file exists, if it does, load values to the mainDictn. If it does not exist, create the file
    try:
        with open(file,"r") as f:
            mainDict = json.load(f)
    except FileNotFoundError:
        open(file, "w")
        with open(file,"r") as firstread:
            mainDict = json.load(firstread)
    except: # This takes care of all other exceptions which might occur such as the file being corrupted, empty, etc
        pass
    
    
    for i in range (numberSample): # Generate the sentences by the number of sample given
        sentence = utils.generator(dictn, length)
        if strDictn not in mainDict:
            mainDict[strDictn] = [sentence]
        else:
            mainList.append(sentence)
            mainDict[strDictn] += mainList
    # Open the file and write the compiled mainDictn
    with open(file,"w") as writefile:
        json.dump(mainDict,writefile)
    
    # Read the content of the  file and see what was write there
    with open (file, "r") as check:
        finalDictn = json.load(check)
        return(finalDictn)    
print(experimenter({"a":.1,"b":.3,"c":.6}, 50, 1))
print(experimenter({"a":.1,"b":.2,"c":.7}, 50, 1))
print(experimenter({"a":.3,"b":.4,"c":.3}, 50, 1))
    

def examiner(file):
    finalDictn = {} # This is the last dictionary to be returned
    editedDictn = {} # Here we will modify the dictionary to get nice keys and values
    counter = 1
    characters = [] # This will store the characters in dictionary key. Eg a, b, c
    
    # Load the json file and assign data to the finalDictn
    with open (file, "r") as check:
            finalDictn = json.load(check)
    
    #print(finalDictn)
    #Here we will be cleaning the keys to get the characters
    for i in finalDictn:
        char = i.replace('}','').replace('{','').replace(',','').replace(':','').replace('\'','').split() # Remove the punctuations in the key
        increment = 0
        while increment < len(char):
            if char[increment] not in characters:
                characters.append(char[increment])
            increment +=2
        dictnKey =(i.split('}'))
        dictnKey[0] = dictnKey[0]+'}'
        key =str(counter)+'.'+"Frequencies"
        length = ",  Length:" + str(dictnKey[1])
        samples = ", Samples:" +str(len(finalDictn[i]))
        counter +=1
        editedDictn[key] = dictnKey[0] + length + samples
        
    # This will display the list of available keys in the dictionary so the user can make a choice
    for i in sorted(editedDictn):
        print(i + editedDictn[i])
    choice = input("Choose Option below, Enter the number eg 3:    ")
    choice = choice+".Frequencies"
    letterDictn ={}
    
    # Check if the entered option by the user is one of the keys in the dictionary. The user can however enter 1 or 2 or 3 for simplication and the program will autocomplete the key
    for i in finalDictn:
        if choice in editedDictn:
            loops =(editedDictn[choice].split(',')[-1].split(':')[-1])
            for j in range(int(loops)):
                for letter in characters:
                    appearance =(finalDictn[i][j]).count(letter)/len(finalDictn[i][j])
                    appearance =  round(appearance, 2)
                    letterDictn[letter] = appearance
                    df = pd.DataFrame(letterDictn, index = list(" "))
                print(df)
                break   # If the dictionary converted into a dataframe successfuly, break from the loop
jsonfile = "textfile.json"
print(examiner(jsonfile))
    
