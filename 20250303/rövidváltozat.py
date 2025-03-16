print("1. feladat:")
terem1=[4,4,0,0,5,6,6,5,0,0,0,4]
[print(f"{i+1}. szék: {"foglalt" if terem1[i]>0 else "üres"}") for i in range(len(terem1))]
print(f"Az 1-es teremben lévő üres helyek száma: {terem1.count(0)}")
print("2. feladat:")
while not(1000<=(alapar:=int(input("Add meg az alapárat [1000...5000]: ")))<=5000): print("Hibás adatbevitel! Próbáld újra...")
print(f"Az 1-es terem bevétele: {sum([alapar*x for x in terem1])} Ft")
print("3. feladat:")
def adatokBeolvasása():
    return [list(map(int, x)) for x in list(map(lambda x: x.rstrip().split(' '), [x for x in open('fogl2.txt','r')]))]
def kedvenc(lista:list):
    filter([print(f"{i+1}. szék: {l[i]} foglalás") for i in range(len(l))], l:=[len(i)-i.count(0) for i in list(zip(*lista))])
    print( f"Legtöbb foglalás: {l.index(max(l))+1}. szék ")
terem2=adatokBeolvasása()
kedvenc(terem2)