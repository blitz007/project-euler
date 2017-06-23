sum=0
fib=[0,1,1]
trm=1
while fib[len(fib)-1]<4000000:
    fib.append(fib[len(fib)-2]+fib[len(fib)-1])
for i in range(0,len(fib)):
    if fib[i]%2==0:
        sum+=fib[i]

print sum
    
    
    
