import tenseal as ts

# Setup TenSEAL context

context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60,40,40,60]
        )

context.generate_galois_keys()
context.global_scale = 2**40

v1 = [0,1,2,3,4]
v2 = [4,3,2,1,0]

# Chiffrement des vecteurs
enc_v1 = ts.ckks_vector(context, v1)
enc_v2 = ts.ckks_vector(context, v2)

result = enc_v1 + enc_v2
res1 = result.decrypt() # [4, 4, 4 ,4]

for val in res1 :
    print(val)

result = enc_v1.dot(enc_v2)

result = enc_v1.dot(enc_v2)
res2 = result.decrypt() # [10]

for val in res2 :
    print(val)


matrix = [
  [73, 0.5, 8],
  [81, -5, 66],
  [-100, -78, -2],
  [0, 9, 17],
  [69, 11 , 10],
]
result = enc_v1.matmul(matrix)
res3 = result.decrypt() # ~ [157, -90, 153]

for val in res3 :
    print(val)

print("Automatic relinearization is:", ("on" if context.auto_relin else "off"))
print("Automatic rescaling is:", ("on" if context.auto_rescale else "off"))
print("Automatic modulus switching is:", ("on" if context.auto_mod_switch else "off"))
                                                                                        
