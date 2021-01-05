'''
Il ROT-15 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare viene sostituita 
con quella posta 15 posizioni più avanti nell'alfabeto. Scrivi una semplice funzione in grado di criptare una 
stringa passata, o decriptarla se la stringa è già stata precedentemente codificata.
'''
def main():
    scelta=2
    while int(scelta)<0 or int(scelta)>1 : 
        scelta=input("0. Criptare una stringa\n1. Decriptare una stringa\n")
    
    stringa=input("Inserire stringa: ")
    if int(scelta)==0:
        stringa=criptare(stringa)
    else:
        stringa=decrpitare(stringa)
    print(stringa)

def criptare(parola):
    letParola=list(parola)
    elemento=0
    while elemento<len(letParola):
        numeroSos=ord(letParola[elemento])+15
        if numeroSos>valoreZ:
            numeroSos=valoreA+(numeroSos-valoreZ)
        letParola[elemento]=chr(numeroSos)
        elemento+=1
    return("".join(letParola))

def decrpitare(parola):
    letParola=list(parola)
    elemento=0
    while elemento<len(letParola):
        numeroSos=ord(letParola[elemento])-15
        if numeroSos<valoreA:
            numeroSos=valoreZ-(valoreA-numeroSos)
        letParola[elemento]=chr(numeroSos)
        elemento+=1
    return("".join(letParola))
    
if __name__ == "__main__":
    valoreA=97
    valoreZ=122
    main()
