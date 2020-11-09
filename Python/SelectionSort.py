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
kmin=0
for elemento in enumerate(lista):
    kmin=elemento
    j=elemento+1
    for j in enumerate(lista):
        if lista[kmin] > lista[j] :
            kmin=j
    temp=0
    if(kmin!=elemento):
        temp=lista[elemento]
        lista[elemento]=lista[kmin]
        lista[kmin]=temp

    

        
