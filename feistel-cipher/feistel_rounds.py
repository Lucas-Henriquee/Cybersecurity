# XOR operation between two binary strings
def xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

# S-BOX from DES 
DES_SBOX = [
    [14, 4, 13, 1, 2, 15, 11, 8,
     3, 10, 6, 12, 5, 9, 0, 7],
]

# Convert 4-bit binary string to S-BOX output
def sbox_substitution(input_bits, box=0):
    row = int(input_bits[0] + input_bits[-1], 2)
    col = int(input_bits[1:3], 2)
    sbox_value = DES_SBOX[box][(row * 4 + col) % 16]
    return format(sbox_value, '04b')

# Round function f: XOR and S-BOX 
def f(right, key):
    xor_result = xor(right, key)
    return ''.join(sbox_substitution(xor_result[i:i+4]) for i in range(0, len(xor_result), 4))

# One round of the Feistel structure
def feistel_round(left, right, key):
    new_left = right
    new_right = xor(left, f(right, key))
    return new_left, new_right

# Encrypt a single binary block using the Feistel cipher
def feistel_encrypt_block(block, round_keys):
    left = block[:len(block)//2]
    right = block[len(block)//2:]
    for key in round_keys:
        left, right = feistel_round(left, right, key)
    return right + left  

# Decrypt a single binary block using the Feistel cipher
def feistel_decrypt_block(block, round_keys):
    left = block[:len(block)//2]
    right = block[len(block)//2:]
    for key in reversed(round_keys):
        left, right = feistel_round(left, right, key)
    return right + left  