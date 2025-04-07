

filename="input3.txt"

def adatokbeolvasasa(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    print(sorok)

    matrix=[]
    for i in range(len(sorok)):
        sor=sorok[i].strip()
        print(f"({sor})")
        szokozok_nelkul=sor.split(" ")
        print(szokozok_nelkul)
        
        szamok=[]
        for j in range(len(szokozok_nelkul)):
            adat=szokozok_nelkul[j]
            print(adat, type(adat))
            szam=int(adat)
            print(szam, type(szam))
            szamok.append(szam)
        print(szamok)
        matrix.append(szamok)
        
    print(matrix)
    return matrix

x=adatokbeolvasasa(filename)
print(x)