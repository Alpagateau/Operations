F=[5,6,7,3,5,6,7,3,1]
L = []
for i in range (len(F)):
    if F[i] not in L:
        L.append(F[i])
print(list(L))

M = []

def plus(L):
    A=[]
    for i in range (len(L)):
        for k in range (len(L)):
            if i>=k:
                continue
            else:
                A+=[L.copy()]
                n=L[i]+L[k]
                if not(n in M):
                    M.append(n)
                A[-1].append(L[i]+L[k])
                A[-1].pop(k)
                A[-1].pop(i)
                main(A[-1])
    return (A)
print(plus(L))

def moins(L):
    B=[]
    for i in range (len(L)):
        for k in range (len(L)):
            if i==k:
                continue
            else:
                if L[k]<=L[i]:
                    c=L[i]
                    d=L[k]
                    B+=[L.copy()]
                    n=c-d
                    if not(n in M):
                        M.append(n)
                    B[-1].append(L[i]-L[k])
                    B[-1].remove(c)
                    B[-1].remove(d)
                    main(B[-1])
                else:
                    continue
    return (B)
print(moins(L))

def fois(L):
    C=[]
    for i in range (len(L)):
        for k in range (len(L)):
            if i==k:
                continue
            if i>k:
                continue
            if i<k:
                C+=[L.copy()]
                n=L[i]*L[k]
                if not( n in M):
                    M.append(n)
                C[-1].append(L[i]*L[k])
                C[-1].pop(k)
                C[-1].pop(i)
                main(C[-1])
    return (C)
print(fois(L))

def diviser(L):
    D=[]
    for i in range (len(L)):
        for k in range (len(L)):
            if i==k:
                continue
            else:
                if L[k]<L[i]:
                    if L[k]==0:
                        continue
                    if L[i]%L[k]==0:
                        c=L[i]
                        d=L[k]
                        D+=[L.copy()]
                        n = c//d
                        if not( n in M):
                            M.append(n)
                        D[-1].append(n)
                        D[-1].remove(c)
                        D[-1].remove(d)
                        main(D[-1])
                    else :
                        continue
                else:
                    continue
    return (D)
print(diviser(L))

def main(L):
    if len(L) <= 1:
        return
    plus(L)
    moins(L)
    fois(L)
    diviser(L)


main(L)
M.sort()
print(M)

k = 0
while k < len(M):
    if M[k] > 999:
        M.remove(M[k])
    else:
        k += 1

print(M)