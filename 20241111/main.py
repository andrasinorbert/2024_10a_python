import my_funcs

print(my_funcs.osszegzes([1,2,3,4,5],lambda x,y:x*y))

import my_funcs as f
import random as r

print(f.osszegzes([1,2,3,4,5],lambda x,y:x*y))
print(f.print("szia"))

from my_funcs import osszegzes

print(osszegzes([1,2,3,4,5],lambda x,y:x*y))



