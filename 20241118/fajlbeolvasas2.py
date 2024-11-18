def be(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    return sorok

def listaClean(lista):
    tisztitottlista=[]
    for sor in lista:
        tisztitottlista.append(sor.strip())
    return tisztitottlista

sorok=be("input2.txt")
tisztott=listaClean(sorok)
print(tisztott)

szamlista=[]
#[szamlista.append(int(i)) for i in tisztott]
for i in tisztott:
    szam=int(i)
    szamlista.append(szam)

print(szamlista)

sum=0
for i in range(len(szamlista)):
    sum+=szamlista[i]
print(sum)