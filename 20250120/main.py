class Adat:
    def __init__(self):
        self.nev=""
        self.szamok=[]
        
lista=list()

a=Adat()
a.nev="Sanyi"
a.szamok=[1,2,3,4,5]
print(f"{a.nev} számai: {a.szamok}")

class Adat2:
    def __init__(self, nev:str,_szamok:list):
        self.nev=nev
        self.szamok=_szamok
        
    def __str__(self):
        return f"[{self.nev}; {self.szamok}]"
    
    def szamok_osszege(self):
        osszeg=0
        for i in range(len(self.szamok)):
            osszeg+=self.szamok[i]
        return osszeg
        
b=Adat2("Eszter",[1,2,3,5,4])
print(f"{b.nev} számai: {b.szamok} számok összege: {b.szamok_osszege()}")
print(b)
l=[1,2,3]
print(l)

l2=["Eszter", "Béla"]

print(str(l2).replace("'", ""))

class SajatLista:
    def __init__(self, lista:list):
        self.lista=lista
    
    def __str__(self):
        return str(self.lista).replace("'", "")
    
    def append(self, item):
        self.lista.append(item)
    
x=SajatLista(["Eszter","Béla", "János"])
print(x)
x.append("Gyuri")
print(x)
x.lista.append("Feri") # igy is lehet használni
