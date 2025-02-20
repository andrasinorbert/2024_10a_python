# 2022.05.03. vizsga

# 3.
# Egy kókuszgolyókat gyártó cégnek öt gyártósora a hét minden napján, a nap összes órájában folya-
# matosan gyártja a kókuszgolyókat. A selejt.txt fájlban a múlt heti termelés alatt előállt selejtes
# kókuszgolyók számai láthatók.

# A fájl első sora a hétfői, a második a keddi, a harmadik a szerdai stb. napon, az egyes gyártósorokon
# keletkezett selejtek számát mutatja (értelemszerűen egy soron belül az 1. oszlop az 1. gyártósort, a
# 2. oszlop a 2. gyártósort stb. jelenti). Így például a vizsgált héten hétfőn összesen 11 db, kedden 7
# db selejtes kókuszgolyó keletkezett.

def adatokBeolvasása(filename):
    file=open(filename, encoding="utf-8")
    sorok=file.readlines()
    file.close()
    
    adatsorok=[]
    for i in range(len(sorok)):
        sor=sorok[i].strip().split(" ")
        for j in range(len(sor)):
            sor[j]=int(sor[j])
        adatsorok.append(sor)
    return adatsorok
    
filename="selejt.txt"

x=adatokBeolvasása(filename)
#print(x)
#for i in range(len(x)):
#    print(x[i])
    
# b)
# Íjon függvényt hatékonyság néven, amelyik visszaadja a hívás helyére azoknak a napoknak
# a számát összesen, amikor egy adott napon belül legalább három olyan gyártósor üzemelt,
# amelyik nem gyártott selejtet! A függvény által visszaküldött napok számát a főprogramban
# kell kiíratni!

def hatékonyság(adatsorok):
    szamlalo=0
    for i in range(len(adatsorok)):
        nullakszama=0
        for j in range(len(adatsorok[i])):
            if adatsorok[i][j]==0:
                nullakszama+=1
        if nullakszama>=3:
            szamlalo+=1
    return szamlalo

def hatékonyság2(adatsorok):
    szamlalo=0
    for i in range(len(adatsorok)):
        nullakszama=adatsorok[i].count(0)
        if nullakszama>=3:
            szamlalo+=1
    return szamlalo

def hatékonyság3(adatsorok):
    szamlalo=0
    for i in range(len(adatsorok)):
        if adatsorok[i].count(0)>=3:
            szamlalo+=1
    return szamlalo

print(f"Hatékony napok száma: {hatékonyság2(x)} db")



print(f"Hatékony napok száma: {hatékonyság3(adatokBeolvasása("selejt.txt"))} db")