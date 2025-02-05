from ember import *

a=Ember("Béla", 12)
print(a.name)
a.name="Balázs"
print(a.getName())
a.setAge(14)
print(a.getAge())

a.iszik()

b=Tanulo("Sára", 18, 123)
print(b.name)
print(b.getName())
b.alszik()
b.tanul()