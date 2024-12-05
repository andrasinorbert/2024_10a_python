#file=open("2024_10a_python/20241202/input1")
# vagy: terminálban: cd .\2024_10a_python\20241202\
file=open("input1")
sor=file.readlines()
file.close()

print(sor)

szoveg_lista=sor[0].split(" ")
print(szoveg_lista)
szamlista=[]
for i in range(len(szoveg_lista)):
    szam=int(szoveg_lista[i])
    szamlista.append(szam)
"""
kicsit máshogy
for i in szoveg_lista:
    szamlista.append(int(i))

[szamlista.append(int(i)) for i in szoveg_lista]
"""
print(szamlista)

s=0
for i in range(len(szamlista)):
    s+=szamlista[i]
print(f"osszeg: {s}")

def filemegnyitas(filename:str)->list[str]:
    """megnyitja a listát, visszatér a sorok listájával

    Args:
        filename (str): file elérési útja

    Returns:
        list[str]: sorokat tartalmazó lista
    """
    file=open(filename)
    lista=file.readlines()
    file.close()
    return lista

def lista_atalakitas(lista:list[str])->list[int]:
    """Mátrix 0. sorából ami szöveges lista, egész számokat készít

    Args:
        lista (list[str]): bemenő lista, mely stringeket tartalmaz

    Returns:
        list[int]: kimenő lista, egész számokat tartalmaz
    """
    sor=lista[0]
    szoveg_lista=sor.split(" ")
    szamlista=[]
    for i in range(len(szoveg_lista)):
        szam=int(szoveg_lista[i])
        szamlista.append(szam)
    return szamlista

filename="input1"
matrix=filemegnyitas(filename)
szamlista=lista_atalakitas(matrix)
print(szamlista)

filename="input2"
matrix=filemegnyitas(filename)
print(matrix)

def lista_atalakitas2(lista:list[str])->list[int]:
    szam_matrix=[]
    for i in range(len(lista)):
        sor=lista[i].strip() 
        szoveg_lista=sor.split(" ")
        szamlista=[]
        for j in range(len(szoveg_lista)):
            szam=int(szoveg_lista[j])
            szamlista.append(szam)
        szam_matrix.append(szamlista)
    return szam_matrix

print(lista_atalakitas2(matrix))