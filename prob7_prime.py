prime=[1,2]
num=3

while len(prime)<10002:
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
            else:
                prime.append(num)
    num+=1

print prime[10000]
    
    
