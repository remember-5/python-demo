# @see https://mofanpy.com/tutorials/data-manipulation/np-pd/np-copy/

import numpy as np

a = np.arange(4)

b = a
c = a
d = b
print(b)
print(c)
print(d)


print(a)
a[0]= 11
print(b)
print(c)
print(d)

print("================================================")

b = a.copy()
print(b)
a[3] = 44
print(a)
print(b)



print("================================================")
