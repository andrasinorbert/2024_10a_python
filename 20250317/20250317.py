"""
1) Kérj be a felhasználótól egy egész számot 5 és 15 közt! Ha rosszat ad meg, kérd be újra!
    a) Készíts egy ekkora méretű listát, s töltsd fel 1 és 5 közti véletlen egész számokkal! Írd ki a listát!
    b) Számold ki, és írd ki a következőket!
        i) összeg
        ii) számtani átlag
        iii) mértani átlag
        iv) szórás
        v) medián
        vi) módusz
        vii) számok szorzata
        viii) páros számok összege
        ix) max érték db száma
        x) 3-mal osztható számok átlaga

3) Olvasd be az "input" fájlt! A számokat számként tárold el, egy könnyen kezelhető adatszerkezetben.
    a) írd ki az oszloponkénti és soronkénti összeget, átlagot, min és max  értéket, valamint számold meg, hogy a legkisebb értékből hány darab van!
    b) írj egy függvényt, mely transzponálja a mátrixot, majd kiírja azt!
    (transzponált jelentése: az első sor lesz az első oszlop, a második sor a második oszlop. Tehát a sorok és oszlopok felcserélését jelenti)
"""
import random
import functools
while not(5<=(db:=int(input("Adj meg egy számot 5 és 15 között! ")))<=15): print("Rosszat adtál meg! Add meg újra!")
print(lista:=[random.randint(1,5) for _ in range(db)])
print(f"összeg: {sum(lista)}")
print(f"számtani átlag: {sum(lista)/len(lista)}")
print(f"mértani átlag: {functools.reduce(lambda x,y:x*y,lista)**(1/len(lista))}")
print(f"szórás: {(sum(map(lambda x: (x-sum(lista)/len(lista))**2, lista))/len(lista))**(1/2)}")
print(f"medián: {sorted(lista[:])[(len(lista))//2] if len(lista)%2==1 else sum(sorted(lista[:])[(len(lista))//2-1:(len(lista))//2+1])/2}")
print(f"módusz: {", ".join(map(str, list(set(filter(lambda x: lista.count(x)==max([ lista.count(i) for i in set(sorted(lista[:]))]),lista)))))}")
print(f"számok szorzata: {functools.reduce(lambda x,y:x*y,lista)}")
print(f"páros számok összege: {sum(filter(lambda x: x%2==0,lista))}")
print(f"max érték db száma: {lista.count(max(lista))}")
print(f"3-mal osztható számok átlaga: {"nincs" if len((felt:=list(filter(lambda x: x%3==0,lista)))) == 0 else sum(felt) / len(felt)}")
# 2) Keresd meg a legnagyobb számot, s írd ki a 2. előfordulásának az indexét!
print(f"legnagyobb elem 2. előfordulásának indexe: {l[1] if len(l:=[i for i in range(len(lista)) if lista[i]==max(lista)])>1 else "nincs második max elem"}")
# 3.
matrix=[list(map(int, x)) for x in list(map(lambda x: x.rstrip().split(' '), [x for x in open('input','r')]))]
print(f"soronkénti összeg: {list(map(sum, matrix))}")
print(f"soronkénti átlag: {list(map(lambda x: sum(x)/len(x), matrix))}")
print(f"soronkénti min: {list(map(min, matrix))}")
print(f"soronkénti max: {list(map(max, matrix))}")
print(f"soronkénti min értékek száma: {[x.count(min(x)) for x in matrix]}")
input_transzponalt=list(zip(*matrix))
print(f"oszloploponként összeg: {list(map(sum, input_transzponalt))}")
print(f"oszloponkénti átlag: {list(map(lambda x: sum(x)/len(x), input_transzponalt))}")
print(f"oszloponkénti min: {list(map(min, input_transzponalt))}")
print(f"oszloponkénti max: {list(map(max, input_transzponalt))}")
print(f"oszloponkénti min értékek száma: {[x.count(min(x)) for x in input_transzponalt]}")