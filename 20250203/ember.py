class Ember:
    def __init__(self, _name:str, _age:int):
        self.name = _name
        self.age = _age
    
    def getName(self)->str:
        return self.name
    
    def getAge(self)->int:
        return self.age
    
    def setName(self, newName:str):
        self.name=newName
    
    def setAge(self, newAge:int):
        self.age = newAge
        
    def eszik(self):
        print(f"{self.name} eszik")
    
    def alszik(self):
        print(f"{self.name} alszik")
        
    def iszik(self):
        print(f"{self.name} iszik")
        
class Tanulo(Ember):
    def __init__(self, _nev:str, _kor:int, _kretaID:int):
        super().__init__(_nev, _kor)
        self.kretaID = _kretaID
    
    def getKretaID(self)->int:
        return self.kretaID
    
    def setKretaID(self, newID:int):
        self.kretaID = newID
        
    def tanul(self):
        print(f"{self.name} tanul")
    
    def jatszik(self):
        print(f"{self.name} jatszik")
        