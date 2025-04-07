

filename="input2.txt"

def adatokbeolvasasa(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    #print(sorok)

    szamok=[]
    for i in range(len(sorok)):
        adat=sorok[i].strip()
        #print(adat, type(adat))
        szam=int(adat)
        #print(szam, type(szam))
        szamok.append(szam)
    #print(szamok)
    return szamok

x=adatokbeolvasasa(filename)
print(x)