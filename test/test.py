import tenseal as ts
import base64


context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60], encryption_type=ts.ENCRYPTION_TYPE.SYMMETRIC)

context.generate_galois_keys()
context.global_scale = 2**40

vec1 = [1,2,3,4,5,6]
vec2 = [7,8,9,10,11,12]

enc_v1 = base64.b64encode(ts.ckks_vector(context, vec1).serialize())
enc_v2 = base64.b64encode(ts.ckks_vector(context, vec2).serialize())

with open("test.bin", 'wb') as f:
    f.write(enc_v1 + b"\n")
    f.write(enc_v2 + b"\n")

vecs = []
with open("test.bin", 'rb') as f:
    vecs = f.readlines()

vecs = [line.rstrip() for line in vecs]

enc_list = []
for vec in vecs :
    print(len(vecs))
    vec_bytes = base64.b64decode(vec)
    enc_list.append(ts.tensors.ckksvector.CKKSVector.load(context, vec_bytes))
for val in enc_list[0] :
    print(val)

print(enc_list[0].decrypt())
print(enc_list[1].decrypt())
