L=[2,3,4,9,6,7]

def somme_simple(L, i, k): #0001
    u=L[i]+L[k]
    L.pop(k)
    L.pop(i)
    L.append(u)
    return L


#avec + :
def plus(L):
    A=L.copy()       
    D=[]                     #0001 -> L [...]
    for i in range (len(L)):
        for k in range (len(L)):
            if i==k:
                continue
            elif i > k:
                continue
            else:
                A = L.copy()
                somme_simple(A, i, k)#00ik -> L[...]
                D.append(A)
    return D

print(plus(L))



#avec multiplication 

def multiplication(L):
    B=L.copy()
    C = []
    for j in range(len(L)):
        for  n in range (len(L)):
            if j==n:
                continue
            if j>n:
                continue
            if j<n:
                B=L.copy()
                v=B[j]*B[n]
                B.pop(n)
                B.pop(j)
                B.append(v)
                C.append(B)     
    return C

print(multiplication(L))


def soustraction(L):
    E=L.copy()
    F = []
    for j in range(len(L)):
        for  n in range (len(L)):
            if j==n:
                continue
            if j>n:
                continue
            if j<n:
                E=L.copy()
                v=E[j]-E[n]
                E.pop(n)
                E.pop(j)
                E.append(v)
                F.append(E)     
    return F


#print(f(L,0,1))    

'''A=[0,9,5,2,3,7,9,4,5]
B=sorted(A)

print(B)'''