def fajlbeolvasas(fajlnev):
    file=open(fajlnev)
    sorok=file.readlines()
    file.close()

    #print(sorok)

    matrix=[]
    for i in range(len(sorok)):
        sor=sorok[i].strip()
        #print(f"sor: {sor}")
        sor_lista=sor.split(";")
        #print(f"lista: {sor_lista}")
        szamlista=[]
        for j in range(len(sor_lista)):
            szamlista.append(int(sor_lista[j]))
        #print(szamlista)
        matrix.append(szamlista)
    #print(matrix)
    return matrix

def sorosszegek(matrix):
    osszegek=[]
    for i in range(len(matrix)):
        sor=matrix[i]
        s=0
        for j in range(len(sor)):
            s+=sor[j]
        osszegek.append(s)
    return osszegek

def oszloposszegek(matrix):
    osszegek=[]
    for i in range(len(matrix[0])):
        s=0
        for j in range(len(matrix)):
            s+=matrix[j][i]
        osszegek.append(s)
    return osszegek
fajlname="input1"
szamok=fajlbeolvasas(fajlname)
print(szamok)
print(sorosszegek(szamok))
print(oszloposszegek(szamok))
