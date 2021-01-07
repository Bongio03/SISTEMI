'''
Scrivi una funzione generatrice di password. La funzione deve generare una stringa alfanumerica di 8 caratteri 
qualora l'utente voglia una password semplice, o di 20 caratteri ascii qualora desideri una password più complicata.
'''
import random
import string

def generaPassword(num):
    casuale=[]
    caratteri=string.ascii_letters +string.digits
    for elemento in range(num): 
        casuale.append(str(random.choice(caratteri)))
    return("".join(casuale))

def main():
    scelta=2
    while int(scelta)<0 or int(scelta)>1 : 
        scelta=input("0. Password semplice (8 caratteri)\n1. Password complicata (20 caratteri):\n")

    if int (scelta)==0:
        password=generaPassword(nCaratteriSemplici)
    else:
        password=generaPassword(nCaratteriComplcati)
    
    print(password)

if __name__== "__main__":
    password=""
    nCaratteriSemplici=8
    nCaratteriComplcati=20
    main()
