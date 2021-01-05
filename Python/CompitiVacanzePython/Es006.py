'''
Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta Terra dal 1880 ad oggi,
proveniente da varie fonti (colonna “Source”). Scrivere un programma che generi un dizionario che 
abbia come chiave l’anno (“Year”) e valore la media aritmetica delle anomalie registrate dalle varie fonti 
durante quell’anno.
Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2) trovi la anomalia massima 
e minima nel periodo compreso tra anno_1 e anno_2.

'''
def caricamentoReg():
    annual=open("annual.csv","r").readlines()
    cntSuc=2
    temperatura=0
    cntStessoAnno=0
    cntReg=0
    registroTemp={}
    for riga in annual[1:]:
        annoSuc=annual[cntSuc].split(",")
        letRiga=riga[:-1].split(",")
        temperatura=temperatura+float(letRiga[2])
        cntStessoAnno+=1
        if int(annoSuc[1])!=int(letRiga[1]):
            media=temperatura/cntStessoAnno
            registroTemp[cntReg]={"Anno":letRiga[1],"Media":media}
            cntReg+=1
            cntStessoAnno=1
            temperatura=0
        if cntSuc< len(annual)-1:
            cntSuc+=1
        else:
            cntSuc=1
    
    return registroTemp


def anomalia(anno1, anno2,reg):
    massima=-100000
    minima=1000
    cntReg=0

    if anno1<anno2:
        anno1,anno2=anno2,anno1
    while int(reg[cntReg]["Anno"])!=int(anno1):
        cntReg+=1
    while int(reg[cntReg]["Anno"])>=int(anno2):
        if massima<reg[cntReg]["Media"]:
            massima=reg[cntReg]["Media"]
        if  minima>reg[cntReg]["Media"]:
            minima=reg[cntReg]["Media"]
        cntReg+=1
    return massima,minima
    

def main():
    regTemp=caricamentoReg()
    print(regTemp)
    anno1=input("Inserire il primo anno: ")
    anno2=input("Inserire il secondo anno: ")
    massima, minima=anomalia(anno1, anno2, regTemp)
    print(f"La massima è: {massima} e la minima è: {minima}")

if __name__ == "__main__":
    main()