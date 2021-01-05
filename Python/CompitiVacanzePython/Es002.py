'''
Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a una NIC, 
composto da 6 coppie di cifre esadecimali separate da due punti.
Un esempio di MAC è 02:FF:A5:F2:55:12.
Scrivi una funzione genera_mac che generi degli indirizzi MAC pseudo casuali.
'''
import random
import string

def genera_mac():
    estrazione=[]
    for elemento in range(numeroCoppie):
        estrazione.append(str(random.choice(string.hexdigits)))
        estrazione.append(str(random.choice(string.hexdigits)))
        if int(elemento)!=5:
            estrazione.append(str(","))

    return("".join(estrazione))

def main():
    mac=""
    mac=genera_mac().split(",")
    mac=(":".join(mac))
    print(mac)

if __name__== "__main__":
    numeroCoppie=6
    main()