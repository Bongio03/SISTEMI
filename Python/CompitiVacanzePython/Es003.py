'''
Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, 
ad esempio:1, 1, 2, 3, 5, 8, 13 (...)
Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, 
entro una soglia specifica impostata dall'utente.
'''
def main():
    scelta=0
    scelta=input("Inserire la soglia della serie di fibonacci da stampare: ")
    a=b=1
    print(a)
    print(b)
    serie(a,b,scelta)

def serie(num1,num2,lim):
    if(int(num1+num2)<int(lim)):
        num1=num1+num2
        num1,num2=num2,num1
        print(num2)
        serie(num1,num2,lim)
    else: 
        return 

if __name__== "__main__":
    main()
