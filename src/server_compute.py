import tenseal as ts
import argparse
import base64

context = None

def load_context(context_file_path):
    # Load context from file
    with open(context_file_path, 'rb') as f:
        bytes_data = f.read()

    context = ts.enc_context.Context.load(bytes_data)

def read_file(filepath):
    vecs = []
    with open(filepath, 'rb') as f:
        vecs = f.readlines()
    vecs = [vec.rstrip() for vec in vecs]
     
    # List that will contain encrypt vectors
    enc_list = []
    for vec in vecs :
        vec_bytes = base64.b64decode(vec)
        enc_list.append(ts.tensors.ckksvector.CKKSVector.load(context,  vec_bytes))
    return enc_list

def mean(enc_list, filename):
    mean_vec = ts.ckks_vector(context, [0] * len(enc_list.shape[0]))
    for enc_row in enc_list:
        mean_vec += enc_row
    mean_vec *= 1/len(enc_list)
    # We add mean to the file to notify the result it represent
    write_enc(mean_vec, "mean_" + filename)

def write_enc(enc_vec, filename):
    with open("./data/" + filename, 'wb') as f:
        b64_enc_vec = base64.b64encode(enc_vec.serialize())
        f.write(b64_enc_vec)

def main(arg1, arg2):
    load_context(arg1)
    enc_list = read_file(arg2)

    # We calculate the mean of each column And write result in b64 file
    mean(enc_list, arg2)

    
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='Path of the context. Context allow operation with encrypted vectors')
    parser.add_argument('arg2', help='Path of a base64 file representing encrypted vectors')
    args = parser.parse_args()

    main(args.arg1, args.arg2)
