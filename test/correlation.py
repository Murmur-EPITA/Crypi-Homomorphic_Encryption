import tenseal as ts
import csv
import pandas as pd

filename = "./data/data.csv"
with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)

    # To skip first line that contains column names
    next(reader)
    data = []

    # Tupple list creation
    for row in reader:
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
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60], encryption_type=ts.ENCRYPTION_TYPE.SYMMETRIC)

context.generate_galois_keys()
context.global_scale = 2**40

enc_tensor = ts.tensors.ckkstensor.CKKSTensor(context, data)

# Calcule de la moyenne 
mean = [0] * 15

for val in data :
    for i in range(len(mean)):
        mean[i] += val[i]
for i in range(len(mean)):
    mean[i] = mean[i] / len(data)

print(mean)
    

