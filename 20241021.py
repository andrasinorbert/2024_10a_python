def osszegzes_osszeadassal(lista:list[int|float])->int|float:
    """
        Összegzés tétele.
        lista: int/float adatokat tárol

        return: az adatok összege
    """
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s

print(osszegzes_osszeadassal([2,3,4,5]))

def osszegzes(lista:list[int|float|str], func)->int|float|str:
    """
        Összegzés tétel általánosítva.
        lista: int/float/str adatokat tárol
        func: az elemek közt végzendő művelet függvénye
        return: tipusa megegyezik a listaelemek tipusával
    """
    s=lista[0]
    for i in range(1,len(lista)):
        s=func(s,lista[i])
    return s

def osszeadas(num1, num2):
    return num1+num2
def szorzas(num1, num2):
    return num1*num2
def osszefuz(str1, str2):
    return str1+str2
print(osszegzes([2,3,4],osszeadas))
print(osszegzes([2,3,4],szorzas))
print(osszegzes(["egy", "ketto"],osszefuz))


def maximumkivalasztas(lista:list[int|float])->tuple[int,int|float]:
    """
        Maximum kiválasztás tétel: az első maximum elem indexét, értékét adja vissza.
        
        Params:
            lista: int/float tartalmaz
        
        Return:
            return[0]: index
            return[1]: max érték
    """
    max_index=0
    max_ertek=lista[0]

    for i in range(1,len(lista)):
        if max_ertek<lista[i]:
            max_ertek=lista[i]
            max_index=i
    return max_index, max_ertek

print(maximumkivalasztas([2,3,43,3]))
print(type(maximumkivalasztas([2,3,43,3])))

def szelsoertek_kivalasztas(lista:list, func:bool)->tuple:
    """
        Max/Min kiválasztás tétel.
        
        Params:
            lista: int/float tartalmaz
            func: 2 paraméteres függvény, mely összehasonlítja
                a jelenlegi max/min értéket a lista adott elemével
                visszatérési érteke: bool
            
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

def kisebb(num1, num2):
    return num1<num2

print(szelsoertek_kivalasztas([2,3,4,3,2,0], kisebb))

# Viszont, miért ne adhatnánk meg ezt az egyszerű függvényt sorfolytonosan a függvényhíváskor?
print(szelsoertek_kivalasztas([2,3,4,3,2,0], lambda num1, num2 :num1<num2))

# Lambda fv: névtelen függvény

# Mennyivel egyszerűbb ez a fv hívás?
# Sokkal látványosabb is
print(osszegzes([1,2,3,4,5], lambda num1, num2: num1+num2))
print(osszegzes([1,2,3,4,5], lambda num1, num2: num1*num2))
print(szelsoertek_kivalasztas([1,2,3,4,5], lambda jelenlegi,listaelem:jelenlegi<listaelem))



# De a lambda függvényt tudjuk nevesíteni is, ha akarjuk:
def osszead(num1, num2):
    return num1+num2

osszead2=lambda num1, num2: num1+num2

# Az osszead és osszead2 ugyanazt csinálja
print(osszead(2,3))
print(osszead2(2,3))

hatvany=lambda num1, num2: num1**num2
print(hatvany(2,3))
negyzet=lambda num: hatvany(num, 2)
print(negyzet(5))
