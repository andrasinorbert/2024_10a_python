

while True:
    listameret=input("Add meg a lista méretét [10...20]: ")
    listameret=int(listameret)
    
    #listameret=int(input("Add meg a lista méretét [10...20]: "))
    
    if listameret>=10 and listameret<=20:
        break
    print("Hibás adatbevitel! Próbáld újra!")
    
elemek=[]
#elemek=list()

import random

for i in range(listameret):
    x=random.randint(1,5)
    elemek.append(x)
    
print("A lista tartalma: ", end="")
print(elemek)

print(f"A lista tartalma: {elemek}")

print("A lista tartalma: [", end="")
for i in range(len(elemek)-1):
    print(elemek[i], end="; ")
print(elemek[-1], end="]\n")

# 2. feladat:

#elemek=[2,3,4,5,1,2,3,4,5,1]

osszeg=0

for i in range(len(elemek)):
    osszeg+=elemek[i]
    
osszeg=0
for i in elemek:
    osszeg+=i
    
osszeg=sum(elemek)

print(f"A listában lévő elemek összege: {osszeg}")

print(f"A listában lévő elemek összege: {sum(elemek)}")

# első maximum elem keresése:
maxelem=elemek[0]
maxindex=0
for i in range(1,len(elemek)):
    if maxelem<elemek[i]:
        maxelem=elemek[i]
        maxindex=i

print(f"A listában lévő legnagyobb elem: {maxelem}, helye: {maxindex}. pozíció")

# utolsó maximum elem keresése:
maxelem=elemek[0]
maxindex=0
for i in range(1,len(elemek)):
    if maxelem<=elemek[i]:
        maxelem=elemek[i]
        maxindex=i

print(f"A listában lévő legnagyobb elem: {maxelem}, helye: {maxindex}. pozíció")

# első maximum:

maxelem=max(elemek)
maxindex=elemek.index(maxelem)

print(f"A listában lévő legnagyobb elem: {maxelem}, helye: {maxindex}. pozíció")

# utolsó maximum

maxelem=max(elemek)
forditottlista=elemek[::-1]
#print(elemek)
#print(forditottlista)

maxelem=max(forditottlista)
"""
utolsó elem indexe: len(elemek)-1
"""
maxindex=len(elemek)-1-elemek.index(maxelem)

print(f"A listában lévő legnagyobb elem: {maxelem}, helye: {maxindex}. pozíció")