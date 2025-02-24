# 3. a)
"""
Írjon függvényt adatokBeolvasása néven, amelyik beolvassa a fájl tartalmát egy megfelelő adatszerkezetbe!
Ügyeljen arra, hogy a havi futásteljesítmények numerikus értékekként
legyenek eltárolva az Ön által választott adatszerkezetben!

ABC-123 782 2138 903 4200 0 0 0 980 3905 2045 655 4495
DEF-456 3162 4372 102 487 3279 0 2238 0 4028 2149 2677 259
"""

def adatokBeolvasása(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    
    adatsorok=[]
    for i in range(len(sorok)):
        lista=sorok[i].strip().split(" ")
        
        sor=[]
        sor.append(lista[0]) # rendszám
        for j in range(1,len(lista)):
            sor.append(int(lista[j]))
        adatsorok.append(sor)
    return adatsorok

x=adatokBeolvasása("fuvarok.txt")
for i in x:
    print(i)
    
# b)
"""
Írjon függvényt nullaKm néven, amely visszaadja a hívás helyére, hogy hány olyan hónap volt
2021-ben a teljes adathalmazban, amikor egy teherautó egy hónapban nulla km-t tett meg! A
nullaKm függvény által visszaküldött darabszám értéket a főprogramban írja ki a példában
látható módon!
Az adatbázisban 29 db 0 km havi futásteljesítményt tartalmazó hónap van.
"""
def nullaKm(adatsorok):
    nullakszama=0
    for i in range(len(adatsorok)):
        for j in range(1, len(adatsorok[i])):
            if adatsorok[i][j]==0:
                nullakszama+=1
    return nullakszama
nulla=nullaKm(x)
print(f"Az adatbázisban {nulla} db 0 km havi futásteljesítményt tartalmazó hónap van.")

def nullaKm2(adatsorok):
    nullakszama=0
    for i in range(len(adatsorok)):
        nullakszama+=adatsorok[i].count(0)
    return nullakszama


def adatokBeolvasása_ver2(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    
    adatsorok=[]
    rendsz=[]
    for i in range(len(sorok)):
        lista=sorok[i].strip().split(" ")
        
        sor=[]
        rendsz.append(lista[0]) # rendszám
        for j in range(1,len(lista)):
            sor.append(int(lista[j]))
        adatsorok.append(sor)
    return rendsz,adatsorok

rendsz, fuvarok=adatokBeolvasása_ver2("fuvarok.txt")
print(rendsz)
print(fuvarok)
print(f"Az adatbázisban {nullaKm2(fuvarok)} db 0 km havi futásteljesítményt tartalmazó hónap van.")




def adatokBeolvasása_ver3(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    
    autok=dict()
    for i in range(len(sorok)):
        lista=sorok[i].strip().split(" ")
        
        sor=[]
        for j in range(1,len(lista)):
            sor.append(int(lista[j]))
        autok[lista[0]]=sor
    return autok

autok=adatokBeolvasása_ver3("fuvarok.txt")
print(autok)

def nullaKm_ver3(autok:dict):
    nullakszama=0
    for fuvarok in autok.values():
        nullakszama+=fuvarok.count(0)
    return nullakszama
print(f"Az adatbázisban {nullaKm_ver3(autok)} db 0 km havi futásteljesítményt tartalmazó hónap van.")



class Auto:
    def __init__(self, _rendsz, _fuvarok):
        self.rendsz=_rendsz
        self.fuvarok=_fuvarok
        
    def getNullakSzama(self):
        return self.fuvarok.count(0)

def adatokBeolvasása_ver4(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    
    autok=[]
    for i in range(len(sorok)):
        lista=sorok[i].strip().split(" ")
        
    
        sor=[]
        for j in range(1,len(lista)):
            sor.append(int(lista[j]))
        
        autok.append(Auto(lista[0], sor))
    return autok

autok=adatokBeolvasása_ver4("fuvarok.txt")

def nullaKm_ver4(autok):
    nullakszama=0
    for i in autok:
        nullakszama+= i.getNullakSzama()
    return nullakszama
print(f"Az adatbázisban {nullaKm_ver4(autok)} db 0 km havi futásteljesítményt tartalmazó hónap van.")

