"""
1. add meg hogy Géza hány kókuszgolyót készített a héten
2. Add meg, hogy kedden hány kókuszgolyó készült
3. Add meg, hogy összesen hány kókuszgolyó készült a héten
4. Add meg, hogy ki készítette a legtöbb kókuszgolyót szerdán
5. Add meg, hogy ki nem készített kókuszgolyót pénteken
"""
import fuggvenyek

(nevek, szamok)=fuggvenyek.fajlbeolvasas("input")
print(fuggvenyek.getNevIndex(nevek, "Zoé"))
print(szamok)
print(f"Zoé értékei: {fuggvenyek.getSzamokFromNev(szamok, nevek,'Zoé')}")

# 1. feladat:
#       1. add meg hogy Géza hány kókuszgolyót készített a héten
gezaSzamai=fuggvenyek.getSzamokFromNev(szamok, nevek, "Géza")
print(gezaSzamai)

s=0
for i in range(len(gezaSzamai)):
    s+=gezaSzamai[i]
print(f"Géza összesen {s} kókuszgolyót készített a héten")

#2. feladat
#       2. Add meg, hogy kedden hány kókuszgolyó készült

napindex=2-1

s=0
for i in range(len(szamok)):
    s+= szamok[i][napindex]
print(f"kedden összesen {s} kókuszgolyó készült")

#3. feladat
#       3. Add meg, hogy összesen hány kókuszgolyó készült a héten

s=0
for i in range(len(szamok)):
    for j in range(len(szamok[i])):
        s+=szamok[i][j]
print(f"összesen {s} kókuszgolyó készült a héten")

#4. feladat
#       4. Add meg, hogy ki készítette a legtöbb kókuszgolyót szerdán

napindex=3-1
maxertek=szamok[0][napindex]
maxindex=0
for i in range(len(szamok)):
    if szamok[i][napindex]>maxertek:
        maxertek=szamok[i][napindex]
        maxindex=i
print(f"{nevek[maxindex]} készítette a legtöbb kókuszgolyót szerdán")

#5. feladat
#       5. Add meg, hogy ki nem készített kókuszgolyót pénteken

napindex=5-1
nemkészitettek=[]
for i in range(len(szamok)):
    if szamok[i][napindex]==0:
        nemkészitettek.append(nevek[i])
for i in range(len(nemkészitettek)):
    print(nemkészitettek[i], sep=", ", end=" ")
print("nem készített kókuszgolyót pénteken")