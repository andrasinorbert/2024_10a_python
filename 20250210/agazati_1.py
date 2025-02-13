# 2022.05.03. vizsga

# 1. a)
# A példában látható módon kérjen be a felhasználótól egy listaméretet! A program csak 5 és
# 25 közötti értéket fogadjon el! Ha a felhasználó által megadott érték nem esik bele a megadott
# tartományba, akkor a program írjon ki egy hibaüzenetet és kérje be újra a listaméretet!


while True:
    meret=int(input("Add meg a lista méretét [5...25]: "))
    if 5 <= meret <= 25:
        break
    print("Hibás adatbevitel! Próbáld újra!")
    
# 1. b)
# Hozzon létre egy üres listát számok néven és töltse fel ezt a listát annyi darab -10 és 10
# közötti egész véletlen számmal, amekkora értéket a felhasználó az a) feladatrészben megadott!

import random

számok=[]

for i in range(meret):
    szam=random.randint(-10, 10)
    számok.append(szam)
    
# 1. c)
# Írja ki a lista tartalmát a példában látható módon!

print(f"A lista tartalma: {számok}")