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

def mean(enc_list):
    mean_vec = ts.ckks_vector(context, [0] * len(data[0]))
    for enc_row in enc_list:
        mean_vec += enc_row
    mean_vec *= 1/len(enc_list)

    return mean_vec

def main(arg1, arg2):
    load_context(arg1)
    enc_list = read_file(arg2)
    return



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='Path of the context. Context allow operation with encrypted vectors')
    parser.add_argument('arg2', help='Path of a base64 file representing encrypted vectors')
    args = parser.parse_args()

    main(args.arg1, args.arg2)
