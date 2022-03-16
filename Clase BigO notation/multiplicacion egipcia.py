A = 41
B = 59
aux = 41
pos= 0
result = 0

listaA = [1,2,4,8,16,32] 
listaB = [59,118,236,472,944,1888] 

listaA.reverse()
listaB.reverse()
print(listaA,listaB)

for number in listaA:
    if aux - number >=0:
        result+= listaB[pos]
        aux-=number
    pos +=1

print(result)
