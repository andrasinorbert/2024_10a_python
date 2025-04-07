
def adatokBeolvasasa(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    #print(sorok, type(sorok))

    adat=sorok[0]
    #print(adat, type(adat))
    szokozok_nelkul=adat.split(" ")
    #print(szokozok_nelkul, type(szokozok_nelkul))

    szamok=[]
    for i in range(len(szokozok_nelkul)):
        #print(szokozok_nelkul[i], type(szokozok_nelkul[i]))
        szam=int(szokozok_nelkul[i])
        #print(szam, type(szam))
        szamok.append(szam)
    #print(szamok)
    return szamok


filename="input1.txt"
x=adatokBeolvasasa(filename)
print(x)
