def szelsoertek_kivalasztas(lista:list, func:bool=lambda x,y: x<y)->tuple:
    """
        Max/Min kiválasztás tétel.
        
        Params:
            lista: int/float tartalmaz
            func: 2 paraméteres függvény, mely összehasonlítja
                a jelenlegi max/min értéket a lista adott elemével
                visszatérési érteke: bool
                default: max ker
            
        Return:
            return[0]: index
            return[1]: szélsőérték
    """
    index=0
    ertek=lista[0]

    for i in range(1,len(lista)):
        if func(ertek, lista[i]):
            ertek=lista[i]
            index=i
    return index, ertek

print(szelsoertek_kivalasztas([2,3,4,5,2]))


"""
    köv óra eleje:
    a lambda fügvényt ha meg akarjuk hívni, akkor nem kapunk "hint"-et, hogy mi milyen tipusú
    Erre egy megoldás a következő:
"""

from typing import Callable
hatvany2: Callable[[int|float, int], int] = lambda x,y: x**y

# Ekkor ha meg akarjuk hívni a hatvany2 függvényt, akkor kiírja a hinteket

# így is írhatunk lambda functiont, ha azonnal szeretnénk paraméterekkel ellátni:

print((lambda x,y:x**y)(2,3))


def osszegzes(lista, func):
    s=lista[0]
    for i in range(1,len(lista)):
        s=func(s,lista[i])
    return s

print(osszegzes([1,2,3,4,5],lambda x,y:x*y))


print(osszegzes(func=lambda x,y:x*y,lista=[1,2,3,4,5]))
print(osszegzes(lista=[1,2,3,4,5],func=lambda x,y:x*y))

print("szia", "hello", "szia", sep="csáó", end="")
print("szevasz","szió", "háj")
print([1,2,3,4,5],[2,3,4,5], sep=" szia ")

lista=[2,3,4,5,6]

[print(x) for x in lista]

elvalaszt=lambda jel="-",db=20:print(jel*db)

[print(x) for x in [1,2,3,4,5]]

elvalaszt("*",10)

for x in lista:
    print(x)
    
elvalaszt()

[print(x) for x in lista]

