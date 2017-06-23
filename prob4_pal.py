a=[]
b=[]
pal=[]
for i in range(900,1000):
    a.append(i)
    b.append(i)

for i in range(0,len(a)):
    for j in range(0,len(b)):
        x=str(a[i]*b[j])
        y=x[::-1]
        if x==y:
            pal.append(a[i]*b[j])

print max(pal)
