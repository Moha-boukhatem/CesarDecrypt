
from AlphabetsFrequency import AlphabetsFrequencyTable
from CryptedTexts import CryptedText


def cesar(text):

    original_tab = AlphabetsFrequencyTable
    tab = []

    alphabet = "abcdefjhijklmnopqrstuvwxyz"

    space = 0
    
    #####    Initialisation

    for i in alphabet : 

        position = ord(i) - 97
        element = []
        element.append(i)
        element.append("0")
        tab.append(element) 


    for caracter in text :
        
        if caracter == " " :

            space+=1
            continue

        position = ord(caracter) - 97
        
        a = int(tab[position][1])
        a+=1
        tab[position][1] = a 

    #### Remplacer le nb de repetition vc % 
    
    len_net = len(text) - space

    for i in tab : 

            i[1]= format(int(i[1])/len_net,'.3f')
    print(tab)
    tab.sort(key=lambda x: x[1],reverse=True)

    

    ##### lettre of original_tab to tab #####
    i = 0
    k = 0
    taille = 15
    while i < taille : 

        k+=ord(tab[i][0]) - ord(original_tab[i][0])
        i+=1

    k = int(k/taille)


    #### Decrypte
    
    for cle in range(k-2,k+3) : 
    
        message =""

        for caracter in text :
            
            if caracter == " " :
                
                message +=" " 
                continue
            
            a = ord(caracter)-cle
            
            if a < 79 : 
                a +=26
            message += chr(a)

        print(message)
        print()
        print()


def Main (): 

    cesar(CryptedText)
