nos=[]
for i in range(1,101):
    nos.append(i)
sum1=0
for i in range(0,len(nos)):
    sum1+=(nos[i]**2)

sum2=(sum(nos)**2)
print abs(sum1-sum2)
