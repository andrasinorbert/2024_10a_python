print("1. feladat:")
terem1=[4,4,0,0,5,6,6,5,0,0,0,4]
[print(f"{i+1}. szék: {"foglalt" if terem1[i]>0 else "üres"}") for i in range(len(terem1))]
print(f"Az 1-es teremben lévő üres helyek száma: {terem1.count(0)}")

for i in range(len(terem1)):
    if terem1[i] > 0:
        print(f"{i+1}. szék: foglalt" )
    else:
        print(f"{i+1}. szék: üres" )
        
c=0
for i in range(len(terem1)):
    if terem1[i] == 0:
        c+=1
print(f"Az 1-es teremben lévő üres helyek száma: {c}")

print("2. feladat:")
while not(1000<=(alapar:=int(input("Add meg az alapárat [1000...5000]: ")))<=5000):
    print("Hibás adatbevitel! Próbáld újra...")
print(f"Az 1-es terem bevétele: {sum([alapar*x for x in terem1])} Ft")

print("3. feladat:")
def adatokBeolvasása():
    return [list(map(int, x)) for x in list(map(lambda x: x.rstrip().split(' '), [x for x in open('fogl2.txt','r')]))]
def kedvenc(lista:list):
    l=[len(i)-i.count(0) for i in list(zip(*lista))]
    [print(f"{i+1}. szék: {l[i]} foglalás") for i in range(len(l))]
    print( f"Legtöbb foglalás: {l.index(max(l))+1}. szék ")
terem2=adatokBeolvasása()
kedvenc(terem2)

def adatokBeolvasása2():
    f=open("fogl2.txt")
    sorok=f.readlines()
    f.close()
    
    adatok=[]
    for i in range(len(sorok)):
        sor=sorok[i]
        sor=sor.strip()
        sor=sor.split(" ")
        
        adat=[]
        for j in range(len(sor)):
            szam=int(sor[j]) 
            adat.append(szam)
        adatok.append(adat)
    return adatok

def kedvenc2(lista):
    foglalasok=[]
    
    for i in range(len(lista[0])):
        foglalasok.append(0)
    
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j]!=0:
                foglalasok[j]+=1
                
    for i in range(len(foglalasok)):
        print(f"{i+1}. szék: {foglalasok[i]} foglalás")
    
    maxertek=foglalasok[0]
    maxindex=0
    for i in range(1,len(foglalasok)):
        if foglalasok[i]>maxertek:
            maxertek=foglalasok[i]
            maxindex=i
    print(f"Legtöbb foglalás: {maxindex+1}. szék")
