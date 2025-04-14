l=[1,2,3,4,5,6]

s=0
for i in range(len(l)):
    s+=l[i]
print(s)

matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(matrix, type(matrix))
osszeg=0
for i in range(len(matrix)):
    sor=matrix[i]
    print(sor, type(sor))
    s=0
    for j in range(len(sor)):
        elem=sor[j]
        print(elem, type(elem))
        s+=elem
    print(s)
    osszeg+=s
print(osszeg)

print(matrix, type(matrix))
osszeg=0
for i in range(len(matrix)):
    sor=matrix[i]
    print(sor, type(sor))
    s=sum(sor)
    osszeg+=s
print(osszeg)

s=0
for j in range(len(matrix[0])): #oszlopokon megyünk végig
    reszosszeg=0
    for i in range(len(matrix)): #sorokon megyünk végig
        reszosszeg+=matrix[i][j]
    print(reszosszeg)

#transzponálás
print(s)
matrix2=[]
for i in range(len(matrix[0])):
    matrix2.append([])

print(matrix2)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix2[j].append(matrix[i][j])
        
print(matrix)
print(matrix2)
for i in range(len(matrix2)):
    s=0
    for j in range(len(matrix2[i])):
        s+=matrix2[i][j]
    print(s)
    
def lista_osszeg(lista):
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s

print(lista_osszeg([2,3,4,5]))

def matrix_osszeg(matrix):
    s=0
    for i in range(len(matrix)):
        s+=lista_osszeg(matrix[i])
    return s

matrix=[[1,2,3],[2,3,4]]
print(matrix_osszeg(matrix))