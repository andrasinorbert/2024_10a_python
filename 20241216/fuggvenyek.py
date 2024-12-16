def fajlbeolvasas(fajlnev, adatelvalasztoChar=" "):
    file=open(fajlnev, encoding="utf-8")
    sorok=file.readlines()
    file.close()

    nevek=[]
    matrix=[]
    for i in range(len(sorok)):
        sor=sorok[i].strip()
        sor_lista=sor.split(adatelvalasztoChar)
        
        nevek.append(sor_lista[0])
        #print(sor_lista)
        szamlista=[]
        for j in range(1,len(sor_lista)):
            szamlista.append(int(sor_lista[j]))
        matrix.append(szamlista)
    return (nevek,matrix)

def getNevIndex(nevek:list[str],keresendonev:str):
    i=0
    while not nevek[i]==keresendonev:
        i+=1
    return i

def getSzamokFromNev(szamokMatrix:list[list[int]],nevek:list[str], keresendoNev:str):
    index=getNevIndex(nevek,keresendoNev)
    return szamokMatrix[index]
