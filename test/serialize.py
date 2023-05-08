import tenseal as ts

# Create a context object
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=4096,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

context.generate_galois_keys()
context.global_scale = 2**40

# Serialize the context object to a file
with open("context_data", "wb") as f:
    context_serialized = context.serialize()
    f.write(context_serialized)

# Load the context object from the file
with open("context_data", "rb") as f:
    context_data = f.read()
    context_deserialized = ts.context.Context.load(context_data)

# Use the deserialized context object
x = ts.ckks_tensor.CKKSTensor(context=context_deserialized, data=[1, 2, 3])
