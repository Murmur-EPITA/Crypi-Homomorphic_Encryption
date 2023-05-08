#!/bin/python

import csv
import tenseal as ts

# Load the CSV file into memory
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
'''
# Initialize a context and a plaintext encoderts
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60], encryption_type=ts.ENCRYPTION_TYPE.SYMMETRIC)

context.generate_galois_keys()
context.global_scale = 2**40

# write context data
with open('context_data.bin', 'wb') as f:
    context_data = context.serialize(save_secret_key = True)
    f.write(context_data)
'''    


# Load the data from file
with open('context_data.bin', 'rb') as f:
    bytes_data = f.read()

context = ts.enc_context.Context.load(bytes_data)

#Check Context
print("Context ")
print("Private Key exist  : " + str(context.has_secret_key()))
print("Private Key Value : " + str(context.secret_key().data))


# Encrypt the data
enc_data_global = []
enc_data_sick = []
enc_data_health = []
count = 0
for row in data :
    count += 1
    enc_val_global = ts.ckks_vector(context, row)
    # En bonne santé
    if (row[-1] == 0):
        enc_val_health = ts.ckks_vector(context, row)
        enc_data_health.append(enc_val_health)
    # Chance d'etre Malade
    else :
        enc_val_sick = ts.ckks_vector(context, row)
        enc_data_sick.append(enc_val_sick)
    # Toutes les données 
    enc_data_global.append(enc_val_global)




# Compute the mean of the age and height columns
final_vec_global = ts.ckks_vector(context, [0] * len(data[0]))
final_vec_sick = ts.ckks_vector(context, [0] * len(data[0]))
final_vec_health = ts.ckks_vector(context, [0] * len(data[0]))

for enc_row in enc_data_global:
   final_vec_global += enc_row
for enc_row in enc_data_sick:
   final_vec_sick += enc_row
for enc_row in enc_data_health:
   final_vec_health += enc_row




final_vec_global *= 1/len(enc_data_global)
final_vec_sick *= 1/len(enc_data_sick)
final_vec_health *= 1/len(enc_data_health)


#Decrypt the results
print("Final All: ", final_vec_global.decrypt())
print("Final Sick: ", final_vec_sick.decrypt())
print("Final Health: ", final_vec_health.decrypt())


def enc_persons(personList) :
    persons = personList.to_list()
    enc_personList = []
    for row in persons :
        enc_person = ts.ckks_vector(context, row)
        enc_personList.append(enc_person)
    return enc_personList

def send_context() :
    # Transform public context
    context_data = context.serialize(save_secret_key = False)
    # send the context 

def send_context() :
    #FIXME
    return

def create_context() :
    #FIXME
    return

def load_context() :
    #FIXME
    return

def send_persons() :
    #FIXME
    return
