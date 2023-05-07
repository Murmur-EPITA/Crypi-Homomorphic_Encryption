#!/bin/python

import csv
import tenseal as ts

# Load the CSV file into memory
filename = "data.csv"
with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    # To skip first line that contains column names
    next(reader)
    data = []

    # Tupple list creation
    for row in reader:
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
encoder = ts.encoder(context)

# Encrypt the data
enc_data = []
for row in data :
    enc_data.append(ts.ckks_vector(context, encoder.encode(row)))

# Compute the mean of the age and height columns
final_vec = ts.ckks_vector(context)
for enc_row in enc_data:
   final_vec += enc_row

final_vec *= 1/len(enc_data)

#Decrypt the results
print("Final teub: ", encoder.decode(final_vec.decrypt()))
