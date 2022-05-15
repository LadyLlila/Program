# Esta función debe identificar y llevar a cabo las gradaciones consonánticas típicas del finlandés
'''
word = input("Inserte un verbo para hacer gradación: " )
numletters =len(word)
lettersInRoot = len(word) -1
'''
def gradacion(txt):
    numletters =len(txt)
    #lettersInRoot = len(txt) -1
    word_End = txt[numletters-4:numletters-1]
    global weakRoot

    #---- PP -> P -> V  -------
    if 'p' in word_End:
        positionWeak = txt.index("p",numletters-4, numletters-1)
        weakForm = "p"
        if  (txt.find("p",numletters-3, numletters-1) != -1) and (txt[positionWeak] == txt[positionWeak+1]):
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+2])
        elif (txt.find("p",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "m"):
            weakForm = "mm"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
        else:
            weakForm = "v"
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+1])
    #---- KK -> K -> -   ||   NK --> NG    ||  LKI -> LJE   || RKI -> RJE   -------------
    elif "k" in word_End:
        positionWeak = txt.index("k",numletters-4, numletters-1)
        weakForm = "k"
        if  (txt.find("k",numletters-3, numletters-1) != -1) and (txt[positionWeak] == txt[positionWeak+1]):
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+2])
        elif (txt.find("k",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "n"):
            positionWeak = txt.index("n",numletters-4, numletters-1)
            weakForm = "ng"
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+2])
        elif (txt.find("k",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "l") and (txt[positionWeak+1] == "i"):
            positionWeak = txt.index("k",numletters-4, numletters-1)
            weakForm = "lje"
            weakRoot = str(txt[0:positionWeak-1] + weakForm)
        elif (txt.find("k",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "r") and (txt[positionWeak+1] == "i"):
            positionWeak = txt.index("k",numletters-4, numletters-1)
            weakForm = "rje"
            weakRoot = str(txt[0:positionWeak-1] + weakForm)
        else:
            weakForm = ""
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+1])
    #---- TT -> T -> D  ||  NT -> NN  || LT -> LL -------
    elif "t" in word_End:
        positionWeak = txt.index("t",numletters-4, numletters-1)
        if  (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "n"):
            weakForm = "nn"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
        elif (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "l"):
            weakForm = "ll"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
        elif (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "r"):
            weakForm = "rr"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
        elif (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak] == txt[positionWeak+1]):
            weakForm = "t"
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+2])
        elif (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "l"):
            weakForm = "ll"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
        else:
            weakForm = "d"
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+1])
        print(weakRoot + "  --> (raíz irregular)")
    elif ("p" not in word_End) or ("k" not in word_End) or ("t" not in word_End):
            print(txt[0:numletters-1] + " --> (raíz regular)")

     #print("\nEl final de la palabra: "  word_End)
   # print("\n la cantidad de letras es: " + str(numletters))
    return weakRoot
#gradacion(word)
