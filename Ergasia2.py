prwtoi=[]
ginomenoprwtwn=[]
for i in range(2,100000):
    stop="false"
    for j in range (2,i):
        if (i%j)==0:
            stop="true"
            break
    if stop=="false":
       prwtoi.append(i)
num=int(input('Δώσε αριθμό'))
while num>100000:
    num=int(input('Δώσε αριθμό'))
if num==1:
  print(num)
stop="false"
i=0
while i<len(prwtoi):
    if num%prwtoi[i]==0:
        ginomenoprwtwn.append(prwtoi[i])
        num=(num/prwtoi[i])
        stop="true"
    else:
        i=i+1
if stop=="false":
    print (num)
else:
    for i in ginomenoprwtwn:
        print ("(",i,")")
        
    

    
    

        
