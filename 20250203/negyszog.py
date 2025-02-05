class Teglalap:
    def __init__(self,oldal1,oldal2):
        self.oldal1=oldal1
        self.oldal2=oldal2
    
    def kerulet(self):
        return (self.oldal1+self.oldal2)*2
    
    def terulet(self):
        return self.oldal1*self.oldal2
    
    def atlo(self):
        return (self.oldal1**2+self.oldal2**2)**(0.5)
    
class Negyzet(Teglalap):
    def __init__(self,oldal):
        super().__init__(oldal, oldal)
        
    
