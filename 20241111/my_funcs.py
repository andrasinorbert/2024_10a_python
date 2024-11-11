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

def print(text):
    return "-"+str(text)+"-"