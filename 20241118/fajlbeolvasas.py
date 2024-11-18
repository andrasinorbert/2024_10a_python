
def be(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    return sorok

"""
sorok=be("input.txt")
[print(i, end="") for i in sorok]

def kiir(x):
    print(x, end="")
    
[kiir(i) for i in sorok]
"""

sorok=be("input.txt")
print(sorok)

"""
szoveg="    hdkagekfgkcaeflh    "
print(szoveg)
tisztitott=szoveg.strip()
print(tisztitott)
"""

"""
tisztitott_lista=[]
for sor in sorok:
    #ez is jó a kövi 2 sor helyett: tisztitott_lista.append(sor.strip())
    x=sor.strip()
    tisztitott_lista.append(x)
    
# [tisztitott_lista.append(sor.strip()) for sor in sorok]
    
print(tisztitott_lista)
"""

def listaClean(lista:list)->list:
    """Whitespace karakterek eltüntetése

    Args:
        lista (list): bemeneti lista

    Returns:
        list: tisztított lista
    """
    tisztitott_lista=[]
    for sor in lista:
        x=sor.strip()
        tisztitott_lista.append(x)
    return tisztitott_lista

sorok=be("input.txt")
tisztitott_sorok=listaClean(sorok)
print(tisztitott_sorok)