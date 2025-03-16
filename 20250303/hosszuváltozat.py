print("1. feladat:")
terem1=[4,4,0,0,5,6,6,5,0,0,0,4]

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
alapar=int(input("Add meg az alapárat [1000...5000]: "))
while not(1000<=alapar<=5000):
    print("Hibás adatbevitel! Próbáld újra...")
    alapar=int(input("Add meg az alapárat [1000...5000]: "))
arak=[]
for i in range(len(terem1)):
    ar=alapar*terem1[i]
    arak.append(ar)

osszeg=0
for i in range(len(arak)):
    osszeg+=arak[i]
print(f"Az 1-es terem bevétele: {osszeg} Ft")


print("3. feladat:")

def adatokBeolvasása():
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

def kedvenc(lista):
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

terem2=adatokBeolvasása()
kedvenc(terem2)
