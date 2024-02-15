L=[1,3,5]

def f(L):
    A=[]
    B=[]
    C=[]
    D=[]
    for i in range (len(L)):
        for k in range (len(L)):
            if i==k:
                continue
            if i>k:
                continue
            if i<k:
                if i==0 and k==1:
                    A.append(L[i]+L[k])
                    B+=L
                    B.append(A[-1])
                    B.pop(k)
                    B.pop(i)
                if i==0 and k==2:
                    A.append(L[i]+L[k])
                    C+=L
                    C.append(A[-1])
                    C.pop(k)
                    C.pop(i)
                if i==1 and k==2:
                    A.append(L[i]+L[k])
                    D+=L
                    D.append(A[-1])
                    D.pop(k)
                    D.pop(i)
    return (L,A,B,C,D)

print(f(L))
f(L)            