import tenseal as ts
import csv
import pandas as pd

filename = "./data/data.csv"
with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)

    # To skip first line that contains column names
    next(reader)
    data = []

    count = 10
    # Tupple list creation
    for row in reader:
        if count < 0:
            break
        count -= 1
        skip = False
        for key, value in row.items():
            if (value == 'NA'):
                skip = True
        if (not skip):
            data.append([float(row["male"]), \
                        float(row["age"]), \
                        float(row["currentSmoker"]), \
                        float(row["cigsPerDay"]), \
                        float(row["BPMeds"]), \
                        float(row["prevalentStroke"]), \
                        float(row["prevalentHyp"]), \
                        float(row["diabetes"]), \
                        float(row["totChol"]), \
                        float(row["sysBP"]), \
                        float(row["diaBP"]), \
                        float(row["BMI"]), \
                        float(row["heartRate"]), \
                        float(row["glucose"]), \
                        float(row["TenYearCHD"]), \
                    ])

# Initialize a context and a plaintext encoderts
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=4096, coeff_mod_bit_sizes=[40, 20, 40], encryption_type=ts.ENCRYPTION_TYPE.SYMMETRIC)

context.generate_galois_keys()
context.global_scale = 2**20

print("1")
enc_tensor = ts.tensors.ckkstensor.CKKSTensor(context, data)
print("2")

# Calcule de la moyenne 
flat_tab = enc_tensor.decrypt()
print("Matrice normal :")
for i in range(enc_tensor.shape[0]):
    row = ""
    for j in range(enc_tensor.shape[1]):
        row += ", " + str(flat_tab.raw[i*enc_tensor.shape[1] + j])
    print(row) 

enc_min = enc_tensor[0]
# calcule des min
i = 1
while i < enc_tensor.shape[0]:
    for j in range(enc_tensor.shape[1]):
        if enc_tensor[i][j] < enc_min[j]:
            enc_min[j] = enc_tensor[i][j]
print(enc_min.decrypt().raw)
            
    

'''
shape = enc_tensor.shape
enc_shape = enc_tensor.reshape([shape[1],shape[0]])
flat_tab = enc_shape.decrypt()

print("Matrice inversé :")
for i in range(enc_shape.shape[0]):
    row = ""
    for j in range(enc_shape.shape[1]):
        row += ", " + str(flat_tab.raw[i*enc_shape.shape[1] + j])
    print(row)
'''


'''
result_enc = ts.ckks_tensor(context, [[0.0, 0.0], [0.0, 0.0]])
print(enc_tensor.shape)
for i in range(enc_tensor.shape[0]):
    row = enc_tensor[i].sub(enc_mean)
    result_enc[i] = row
print("mean sub : ", result_enc.decrypt())
'''
