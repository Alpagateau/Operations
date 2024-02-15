L=[1,2,3]
#juste avec +
def f(L):
    L=[1,2,3]
    for i in range (len(L)):
        for k in range (len(L)):
            if i==k:
                continue
            elif i > k:
                continue
            else:
                u=L[i]+L[k]
                L.append(u)
    return L

print(f(L))    

