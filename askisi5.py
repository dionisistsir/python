harshad=[]
harsginom=[]
for i in range(1,1001):
    athr=0
    gin=1
    for j in str(i):
        athr+=int(j)
        gin*=int(j)
    if (i%athr==0):
        harshad.append(i)
    if (gin!=0):
        if (i%gin==0):
            harsginom.append(i)
print harshad
print harsginom
