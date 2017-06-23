nos=[]
for i in range(0,5000):
    x=[]
    for j in range(1,11):
        x.append(i%j)

    if sum(x)==0:
        nos.append(i)

print min(nos)


    
        
        
        
    
        
    

    
