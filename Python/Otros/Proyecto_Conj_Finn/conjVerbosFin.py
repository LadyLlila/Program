#Este programa tiene por objetivo conjugar los diferentes tipos de verbos finlandeses.

#Función gradación de verbos: encuentra los patrones de irregularidad y los modifica a su forma apropiada
def gradacion(txt):
    global weakRoot
    numletters =len(txt)
    #lettersInRoot = len(txt) -1
    word_End = txt[numletters-4:numletters-1]
        #---- PP -> P -> V  -------
    if 'p' in word_End:
        positionWeak = txt.index("p",numletters-4, numletters-1)
        weakForm = "p"
        if  (txt.find("p",numletters-3, numletters-1) != -1) and (txt[positionWeak] == txt[positionWeak+1]):
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+2])
            return weakRoot
        elif (txt.find("p",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "m"):
            weakForm = "mm"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
            return weakRoot
        else:
            weakForm = "v"
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+1])
            return weakRoot
    #---- KK -> K -> -   ||   NK --> NG    ||  LKI -> LJE   || RKI -> RJE   -------------
    elif "k" in word_End:
        positionWeak = txt.index("k",numletters-4, numletters-1)
        weakForm = "k"
        if  (txt.find("k",numletters-3, numletters-1) != -1) and (txt[positionWeak] == txt[positionWeak+1]):
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+2])
            return weakRoot
        elif (txt.find("k",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "n"):
            positionWeak = txt.index("n",numletters-4, numletters-1)
            weakForm = "ng"
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+2])
            return weakRoot
        elif (txt.find("k",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "l") and (txt[positionWeak+1] == "i"):
            positionWeak = txt.index("k",numletters-4, numletters-1)
            weakForm = "lje"
            weakRoot = str(txt[0:positionWeak-1] + weakForm)
            return weakRoot
        elif (txt.find("k",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "r") and (txt[positionWeak+1] == "i"):
            positionWeak = txt.index("k",numletters-4, numletters-1)
            weakForm = "rje"
            weakRoot = str(txt[0:positionWeak-1] + weakForm)
            return weakRoot
        else:
            weakForm = ""
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+1])
            return weakRoot
    #---- TT -> T -> D  ||  NT -> NN  || LT -> LL -------
        positionWeak = txt.index("t",numletters-4, numletters-1)
    elif "t" in word_End:
        positionWeak = txt.index("t",numletters-4, numletters-1)
        if  (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "n"):
            weakForm = "nn"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
            return weakRoot
        elif (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "l"):
            weakForm = "ll"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
            return weakRoot
        elif (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "r"):
            weakForm = "rr"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
            return weakRoot
        elif (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak] == txt[positionWeak+1]):
            weakForm = "t"
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+2])
            return weakRoot
        elif (txt.find("t",numletters-3, numletters-1) != -1) and (txt[positionWeak-1] == "l"):
            weakForm = "ll"
            weakRoot = str(txt[0:positionWeak-1] + weakForm + txt[positionWeak+1])
            return weakRoot
        else:
            weakForm = "d"
            weakRoot = str(txt[0:positionWeak] + weakForm + txt[positionWeak+1])
            return weakRoot
        print(weakRoot + "  --> (raíz irregular)")
    elif ("p" not in word_End) or ("k" not in word_End) or ("t" not in word_End):
        weakRoot = str(txt[0:numletters-1])
        #print(txt[0:numletters-1] + " --> (raíz regular)")
        return weakRoot

     #print("\nEl final de la palabra: "  word_End)
     #print("\n la cantidad de letras es: " + str(numletters))
    else:
        return weakRoot

#----------:: INPUT (1 VERBO) :---------------------
word = input("Inserte verbo a conjugar ")

#print("La palabra a conjugar es", word)

wordLength = len(word)
wordend =  word[-4:wordLength]

#----------:: BLOQUE RECONOCIMIENTO ::------------------------------------------------
VT = 0
if ('stä' in wordend or 'sta' in wordend) or ('lä' in wordend or 'la' in wordend) or ('nä' in wordend or 'na' in wordend) or ('rä' in wordend or 'ra' in wordend):
    VT= 3 
elif 'da' in wordend or 'dä' in wordend:
    VT= 2
else:
    if ('ta' in wordend) or ('tä' in wordend) and (word[len(word)-1] != "a") and (word[len(word)-1] != "ä"):
        if ("ita" in wordend) or ("itä" in wordend):
            VT = 5
        elif ("eta" in wordend) or ("etä" in wordend):
            VT = 6
        else:
            VT= 4
    else: 
        VT=1

global verbRoot
print("--> Verbo tipo: " + str(VT))
#---------:: Verbtyyppi 1 ::---------------------------------
if VT == 1:
    gradacion(word)
    verbRoot = weakRoot
    strongRoot = word[0:len(word)-2]
    print("--> Raíz del verbo: " + verbRoot)
    print("Minä  " + verbRoot + "n")
    print("Sinä  " + verbRoot + "t")
    print("Hän   " + strongRoot + word[-2])
    print("Me    " + verbRoot + "mme")
    print("Te    " + verbRoot + "tte")
    if ('a' in word) or ('o' in word) or ('u' in word):
        print("He    " + strongRoot + "vat")
    else:
        print("He    " + strongRoot + "vät")

if VT == 2:
    lettersInRoot = len(word) -2
    VerbRoot = word[0:lettersInRoot]
    print("--> Raíz del verbo: " + VerbRoot + "\n")
    print("Minä  " + VerbRoot + "n")
    print("Sinä  " + VerbRoot + "t")
    print("Hän   " + VerbRoot)
    print("Me    " + VerbRoot + "mme")
    print("Te    " + VerbRoot + "tte")
    if ('a' in word) or ('o' in word) or ('u' in word):
        print("He    " + VerbRoot + "vat")
    else:
        print("He    " + VerbRoot + "vät")

if VT == 3:
    VerbRoot = word[0:len(word)-2]
    print("--> Raíz del verbo: " + VerbRoot + "e" "\n")
    print("Minä  " + VerbRoot + "e" "n")
    print("Sinä  " + VerbRoot + "et")
    print("Hän   " + VerbRoot + "ee")
    print("Me    " + VerbRoot + "emme")
    print("Te    " + VerbRoot + "ette")
    if ('a' in word) or ('o' in word) or ('u' in word):
        print("He    " + VerbRoot + "evat")
    else:
        print("He    " + VerbRoot + "evät")

if VT == 4:
    verbRoot = str(word[0:len(word)-2] + word[len(word)-1])
    print("--> Raíz del verbo: " + verbRoot)
    print("Minä  " + verbRoot + "n")
    print("Sinä  " + verbRoot + "t")
    if verbRoot[-1] == verbRoot[-2]:
        print("Hän   " + verbRoot)
    else:
        print("Hän   " + verbRoot+ word[-1])
    print("Me    " + verbRoot + "mme")
    print("Te    " + verbRoot + "tte")
    if ('a' in word) or ('o' in word) or ('u' in word):
        print("He    " + verbRoot + "vat")
    else:
        print("He    " + verbRoot + "vät")

if VT == 5:
    verbRoot = str(word[0:len(word)-2])
    print("--> Raíz del verbo: " + verbRoot)
    print("Minä  " + verbRoot + "tsen")
    print("Sinä  " + verbRoot + "tset")
    print("Hän   " + verbRoot+ "tsee")
    print("Me    " + verbRoot + "tsemme")
    print("Te    " + verbRoot + "tsette")
    if ('a' in word) or ('o' in word) or ('u' in word):
        print("He    " + verbRoot + "tsevat")
    else:
        print("He    " + verbRoot + "tsevät")

# ¡ OCURRE ALGO! Algunos verbos no son reconocidos como VT =5, sino como VT =1