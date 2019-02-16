def sumintervals(lista):
    x=[]
    for i in lista:
        m=len(i)
        for j in range(i[0],i[m-1]):
            x.append(int(j))
    print (len(set(x)));


    
