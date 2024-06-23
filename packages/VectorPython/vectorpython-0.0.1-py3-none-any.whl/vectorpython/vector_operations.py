
# Add Vectors
def add_vectors(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

# Subtract Vectors
def sub_vectors(vector1, vector2):
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

# Multiply Vectors
def mult_vectors(vector1, vector2):
    return [v1 * v2 for v1, v2 in zip(vector1, vector2)]