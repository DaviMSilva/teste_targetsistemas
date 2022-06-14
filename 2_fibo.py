#fibonace

def sequenciaFibo(num):
    listaFibo = []
    i =0
    fiboNum = 0
    while(fiboNum < num):
        
        
        if i == 0 or i == 1:
            
            listaFibo.append(i)
            
        else:
            fiboNum = listaFibo[i-1] + listaFibo[i-2]
            listaFibo.append(fiboNum)

        i+=1
            
    print(listaFibo)    

    if listaFibo.count(num):
        print(num, " Faz parte da Sequencia Fibo")
    else:
         print(num, "Não Faz parte da Sequencia Fibo")


    
sequenciaFibo(100)
    