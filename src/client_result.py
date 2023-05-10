import tenseal as ts
import argparse
import base64

def load_context(filepath):
    # Load the data from file
    with open(filepath, 'rb') as f:
        context_data = f.read()
        context = ts.enc_context.Context.load(context_data)
    return context


def read_file(filename, context):
    with open('./data/results/' + filename, 'rb') as f:
        vec_data = f.read()
        vec_bytes = base64.b64decode(vec_data)
        enc_vec = ts.tensors.ckksvector.CKKSVector.load(context, vec_bytes)
    return enc_vec


        
def main(arg1, arg2):
    context = load_context(arg1)
    enc_vec = read_file(arg2, arg1)

    print(enc_vec.decrypt())

    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='Path of the private context')
    parser.add_argument('arg2', help='''Name of the file send to the server
    previously. Ex if your file was in ../../Doc/file.b64 the Name is :
    file.b64''')
    args = parser.parse_args()

    main(args.arg1, args.arg2)
