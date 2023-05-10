#!/bin/python

import csv
import base64
import tenseal as ts
from os import makedirs
from utils.Person import *


def enc_persons(personList, context):
    persons = personList.to_list()
    enc_personList = []
    for row in persons :
        enc_person = ts.ckks_vector(context, row)
        enc_personList.append(enc_person)
    return enc_personList

def init_context(privkeyPath=None, publickeyPath=None):
    # Create key files
    if (not privkeyPath) or (not publickeyPath):
        # Initialize a context
        context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=4096, coeff_mod_bit_sizes=[40, 20, 40], encryption_type=ts.ENCRYPTION_TYPE.SYMMETRIC)

        context.generate_galois_keys()
        context.global_scale = 2**20

        keysPath = "/data/keys"
        makedirs(keysPath, exist_ok=True)

        # write private context data
        with open(keysPath+'/privContext.bin', 'wb') as f:
            context_data = context.serialize(save_secret_key = True)
            f.write(context_data)

        # write public context data, N.B.: this filename is also used in docker_server shell script
        with open(keysPath+'/pubContext.bin', 'wb') as f:
            context_data = context.serialize(save_secret_key = False)
            f.write(context_data)
    else :
        # Load the data from file
        with open(privkeyPath, 'rb') as f:
            context_data = f.read()
            context = ts.enc_context.Context.load(context_data)
    return context


def write_persons(personList, context, filename):
    # Encrypt person list
    enc_personlist = enc_persons(personList, context)

    cipherPath = "/data/cipher/"
    makedirs(cipherPath, exist_ok=True)

    # Encoding encrypt vector to add a separator in file
    with open(cipherPath + filename + ".b64", 'wb') as f:
        for enc_person in enc_personlist:
            b64_person = base64.b64encode(enc_person.serialize())
            f.write(b64_person + b"\n")

if __name__ == '__main__':
    # Used to create context files (public one will be for the server to compute stats on ciphered data, private to decrypt the result on client)
    context = init_context()

    # We are in the client container, load PersonList
    complete, sick, healthy = PersonList.from_csv("/data/framingham_heart_disease_raw.csv")

    # Encrypt data in a file that will be sent to server. If you change filename, change it in docker_server shell script also
    write_persons(complete, context, filename='enc_data')
