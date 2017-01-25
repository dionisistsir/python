lista=raw_input("gemise tin lista : ")
pinakas=[]
tlista=""
k=0
for i in range(len(lista)):
    if (lista[i]!="0"):
        pinakas.append(lista[i])
    else:
        k+=1
for i in range(k):
    pinakas.append("0")
for i in range(len(pinakas)):
    tlista+=pinakas[i]
print tlista
