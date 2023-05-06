import numpy as np
from Pyfhel import Pyfhel

HE = Pyfhel()

HE.contextGen(scheme='bfv', n=2**14, t_bits=20)
keypair = HE.keyGen()
print("Context :")
print(HE)

val1 = np.array([1])
val2 = np.array([2])
val3 = np.array([3])
val4 = np.array([4])

arr =  [val1,val2,val3,val4]
carr = []

for val in arr :
    cval = HE.encryptInt(val)
    carr.append(cval)

csum = HE.encryptInt(np.array([0]))
for cval in carr :
    csum = csum + cval

csum2 = carr[0] + carr[1] + carr[2] + carr[4]

cmean = csum2 / len(carr)

res = HE.decryptInt(csum2)
#mean = HE.decryptInt(cmean)

print("Le chiffré est :")
print(csum2)

print("result is : ")
print(res)
'''
print("The mean is :")
print(mean)
'''

