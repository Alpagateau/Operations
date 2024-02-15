L=[1,2,3]
#juste avec +
def f(L):
    L=[1,2,3]
    for i in range (len(L)):
        u=L[i]+L[i+1]
        L.append(u)
    return L

print(f(L))    

