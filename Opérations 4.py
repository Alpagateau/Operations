import time
from newNumb import *

L=[nb(1),nb(2),nb(3),nb(10)]

def verification(A):
    l=len(A)
    for i in range (l):
        if A[l-i-1]>999 or A[l-i-1]<0:
            A.pop(l-i-1)
    return A

def plus(L):
    A = []
    for i in range(len(L)):
        for k in range(i + 1, len(L)):  # Commence à l'index suivant de i
            n = L[i] + L[k]
            if n not in M :
                if n<999:
                    M.append(n)
            A.append(L + [n])    # Ajoute la nouvelle liste et L à A
            A[-1].pop(k)
            A[-1].pop(i)
            main(verification(A[-1]))         # On rapelle la fonction main avec la dernière nouvelle liste créée
    return A
#print(plus(L))

def moins(L):
    B=[]
    for i in range (len(L)):
        for k in range (len(L)):
            if k==i:
                continue
            n=L[i]-L[k]
            if n not in M:
                if 0<=n<999:
                    M.append(n)
            B.append(L+[n])         # Ajoute la nouvelle liste et L à B
            B[-1].pop(k)
            B[-1].pop(i)
            main(verification(B[-1]))          # On rapelle la fonction main avec la dernière nouvelle liste créée
    return (B)
#print(moins(L))

def fois(L):
    C = []
    for i in range(len(L)):
        for k in range(i + 1, len(L)):  # Commence à l'index suivant de i
            n = L[i] * L[k]
            if n not in M:
                if n<999:
                    M.append(n)
            C.append(L + [n])  # Ajoute la nouvelle liste et L à C
            C[-1].pop(k)
            C[-1].pop(i)
            main(verification(C[-1]))        # On rapelle la fonction main avec la dernière nouvelle liste créée
    return C
#print(fois(L))

def diviser(L):
    D = []
    for i in range(len(L)):
        for k in range(len(L)):  # Commence à l'index suivant de i
            if L[k] < L[i]:
                if L[k] == 0:           # pour éviter la division par zéro
                    continue
                if L[i] % L[k] == 0:
                    c = L[i]
                    d = L[k]
                    n = c // d
                    if n not in M :
                        if n<999:
                            M.append(n)
                    D.append(L + [n])  # Ajoute la nouvelle liste et L à D
                    D[-1].remove(c)
                    D[-1].remove(d)
                    main(verification(D[-1]))       # On rapelle la fonction main avec la dernière nouvelle liste créée
    return D
# print(diviser(L))


M = []

def main(L):
    if len(L) <= 1:             # liste d'un seul élément -> stop
        return
    plus(L)
    moins(L)
    fois(L)
    diviser(L)

main(L)
M.sort()                        # pour mettre dans l'ordre


# suppression des éléments non-conformes

k = 0
while k < len(M):
    if M[k] > 999 or M[k]<0:
        M.remove(M[k])
    else:
        k += 1

print(M, len(M))

# compteur de temps

t = time.monotonic()
print("Le programme a mis (en secondes) : ", time.monotonic() - t)


