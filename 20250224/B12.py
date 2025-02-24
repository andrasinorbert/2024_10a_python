# 1.a)
"""
A példában látható módon kérjen be a felhasználótól egy listaméretet! A program csak 10 és
20 közötti értéket fogadjon el! Ha a felhasználó által megadott érték nem esik bele a megadott
tartományba, akkor a program írjon ki egy hibaüzenetet és kérje be újra a listaméretet!
Add meg a lista méretét [10...20]: 25
Hibás adatbevitel! Próbáld újra!
"""

while True:
    meret=int(input("Add meg a lista méretét [10...20]: "))
    if 10<=meret<=20:
        break
    print("Hibás adatbevitel! Próbáld újra!")

meret=int(input("Add meg a lista méretét [10...20]: "))
while 10>meret or meret>20:
    print("Hibás adatbevitel! Próbáld újra!")
    meret=int(input("Add meg a lista méretét [10...20]: "))
# b)
"""
Hozzon létre egy üres listát elemek néven és töltse fel ezt a listát annyi darab 1 és 5 közötti
egész véletlen számmal, amekkora értéket a felhasználó az a) feladatrészben megadott!
"""
import random as r
elemek=list()
for i in range(meret):
    elemek.append(r.randint(1,5))

# c)
"""
Írd ki a lista tartalmát a példában látható módon!
A lista tartalma: [1, 1, 5, 2, 3, 2, 4, 1, 4, 5, 3, 1]
"""
print(f"A lista tartalma: {elemek}")

# 2. a)
"""
A példában látható módon írja ki a listában lévő elemek összegét!
A listában lévő elemek összege: 32
"""
osszeg=0
for i in range(len(elemek)):
    osszeg+=elemek[i]
print(f"A listában lévő elemek összege: {osszeg}")

osszeg=0
for i in elemek:
    osszeg+=i
print(f"A listában lévő elemek összege: {osszeg}")


print(f"A listában lévő elemek összege: {sum(elemek)}")

# b)
"""
A példában látható módon írja ki, hogy melyik a listában lévő legnagyobb szám és az hányadik
pozícióban szerepel a listában! A program az „első legnagyobb” számot adja meg!
A listában lév˝o legnagyobb elem: 5, helye: 3. pozíció
"""
legnagyobb=elemek[0]
hely=0
for i in range(1,len(elemek)):
    if elemek[i]>legnagyobb:
        legnagyobb=elemek[i]
        hely=i
print(f"A listában lévő legnagyobb elem: {legnagyobb}, helye: {hely+1}. pozíció")

legnagyobb=max(elemek)
print(f"A listában lévő legnagyobb elem: {legnagyobb}, helye: {elemek.index(legnagyobb)+1}. pozíció")

print(f"A listában lévő legnagyobb elem: {max(elemek)}, helye: {elemek.index(max(elemek))+1}. pozíció")