'''
void selectionSort(int v[],int n){
    int k,kmin,j;
    for(k=0;k<n-1;k++) {
        kmin=k;
        for(j=k+1;j<n;j++){
            if(v[kmin]>v[j])
                kmin=j;
        }
        if(kmin!=k)
            scambio(&v[k],&v[kmin]);
    }
    return;
}
'''

lista=[88,6,49,22,99,12,1]
print(lista)

for k in range(len(lista)):
    kmin=k
    for j in range(k+1,len(lista)):
        if lista[kmin] > lista[j] :
            kmin=j
    if(kmin!=k):
        lista[kmin] , lista[k] = lista[k] , lista[kmin]

print(lista)

    

        
