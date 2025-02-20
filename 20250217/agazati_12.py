# 2022.05.03. vizsga

# 1. a)
# A példában látható módon kérjen be a felhasználótól egy listaméretet! A program csak 5 és
# 25 közötti értéket fogadjon el! Ha a felhasználó által megadott érték nem esik bele a megadott
# tartományba, akkor a program írjon ki egy hibaüzenetet és kérje be újra a listaméretet!


while True:
    meret=int(input("Add meg a lista méretét [5...25]: "))
    if 5 <= meret <= 25: break
    print("Hibás adatbevitel! Próbáld újra!")
    
# 1. b)
# Hozzon létre egy üres listát számok néven és töltse fel ezt a listát annyi darab -10 és 10
# közötti egész véletlen számmal, amekkora értéket a felhasználó az a) feladatrészben megadott!

import random

számok=[random.randint(-10, 10) for _ in range(meret) ]
    
# 1. c)
# Írja ki a lista tartalmát a példában látható módon!

print(f"A lista tartalma: {számok}")

# 2. 
# Írjon programot, amelyik megoldja a következő feladatokat! A feladatok megoldásához használd fel
# az 1. feladatban létrehozott számok listát! Amennyiben nem sikerült megoldanod az 1. feladatot,
# akkor hozd létre a programban a számok listát és kézzel írj bele 10 darab -10 és 10 közötti egész
# számot!

# 2. a)
# A példában látható módon írja ki a listában lévő elemek összegét!

#megoldás1
osszeg=0
for i in range(len(számok)):
    osszeg+=számok[i]

#megoldás2
osszeg=0
for i in számok:
    osszeg+=i

#megoldás3
osszeg=sum(számok)

print(f"A listában lévő elemek összege: {osszeg}")

# 2. b)
# A példában látható módon írja ki, hogy igaz-e az az állítás, hogy a listában több 0 szám
# szerepel, mint negatív érték!

#megoldás1
nullakszama=0
for i in range(len(számok)):
    if számok[i]==0:
        nullakszama+=1
print(f"A listában lévő 0 elemek száma: {nullakszama}")
negativakszama=0
for i in range(len(számok)):
    if számok[i]<0:
        negativakszama+=1
print(f"A listában lévő negatív elemek száma: {negativakszama}")
        
#megoldás2
nullakszama=0
negativakszama=0
for i in range(len(számok)):
    if számok[i]==0:
        nullakszama+=1
    elif számok[i]<0:
        negativakszama+=1
print(f"A listában lévő 0 elemek száma: {nullakszama}")
print(f"A listában lévő negatív elemek száma: {negativakszama}")

#megoldás3
nullakszama=számok.count(0)
negativakszama=len(list(filter(lambda x:x<0, számok)))
print(f"A listában lévő 0 elemek száma: {nullakszama}")
print(f"A listában lévő negatív elemek száma: {negativakszama}")

#eldöntés
if nullakszama>negativakszama:
    print("Igaz az állítás!")
else:
    print("Nem igaz az állítás!")

print(f"{'Nem igaz' if nullakszama<=negativakszama else 'Igaz'} az állítás!")